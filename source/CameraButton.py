import tkinter as tk
import os
import subprocess
import time
import threading
import logging

from ppadb.client import Client as AdbClient

class CameraButton(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.bind("<space>", self.captureByKey)
        self.pack()
        self.columnconfigure(0, weight = 1)
        self.remote_connection = tk.IntVar()
        self.create_widgets()
        self.client = None
        self.device = None
        self.timer = None

    def create_widgets(self):
        # row = 0
        self.connectButton = tk.Button(self)
        self.connectButton["text"] = "Connect"
        self.connectButton["command"] = self.connection
        self.connectButton.grid(row=0, column=0, sticky = tk.W + tk.E, columnspan=1)

        self.remoteCheckButton = tk.Checkbutton(self, variable=self.remote_connection)
        self.remoteCheckButton["text"] = "Remote connection"
        self.remoteCheckButton.grid(row=0, column=1)

        # row = 1
        self.killButton = tk.Button(self)
        self.killButton["text"] = "Kill server"
        self.killButton["command"] = self.kill_server
        self.killButton.grid(row=1, column=0, sticky = tk.W + tk.E, columnspan=1)

        self.scrcpyButton = tk.Button(self)
        self.scrcpyButton["text"] = "scrcpy"
        self.scrcpyButton["command"] = self.scrcpy
        self.scrcpyButton.grid(row=1, column=1, sticky = tk.W + tk.E, columnspan=2)

        # row = 2
        self.captureButton = tk.Button(self)
        self.captureButton["text"] = "Capture"
        self.captureButton["command"] = self.capture
        self.captureButton.grid(row=2, column=0, columnspan=3, sticky = tk.W + tk.E)

        # row = 3
        self.label = tk.Label(self, text = "Time button (Tick:sec)", width=30)
        self.label.grid(row=3, column=0, sticky = tk.W + tk.E, columnspan=3)

        # row = 4
        self.timeEntry = tk.Entry(self)
        self.timeEntry.insert(0,'3')
        self.timeEntry.grid(row=4, column=0, sticky = tk.W + tk.E + tk.N + tk.S)

        self.startButton = tk.Button(self, width=10)
        self.startButton["text"] = "Start"
        self.startButton["command"] = self.start
        self.startButton.grid(row=4, column=1, sticky = tk.W + tk.E)

        self.stopButton = tk.Button(self, width=10)
        self.stopButton["text"] = "Stop"
        self.stopButton["command"] = self.stop
        self.stopButton.grid(row=4, column=2, sticky = tk.W + tk.E)

    def connection(self):
        os.system("adb usb")
        time.sleep(3)
        if self.remote_connection.get():
            # remote connect
            print("remote connect")
            self.client = AdbClient()
            self.device = self.client.devices()[0]
            address = self.get_ip_addr()
            os.system("adb tcpip 5678")
            time.sleep(5)
            self.client = AdbClient("127.0.0.1", 5037)
            self.client.remote_connect(address, 5678)
            print(self.client.devices())
            self.device = self.client.devices()[1]
        else:
            print("connect")
            self.client = AdbClient()
            self.device = self.client.devices()[0]

    def kill_server(self):
        os.system("adb kill-server")
        time.sleep(3)
        os.system("adb start-server")

    def scrcpy(self):
        subprocess.Popen(["scrcpy"])

    def captureByKey(self, event=None):
        self.capture()

    def capture(self):
        print("capture")
        if self.device:
            self.device.input_keyevent("KEYCODE_CAMERA")
        if self.timer:
            self.start()

    def start(self):
        timer_tick = int(self.timeEntry.get())
        self.timer = threading.Timer(timer_tick, self.capture)
        self.timer.start()

    def stop(self):
        print("stop")
        if self.timer:
            self.timer.cancel()
            self.timer = None

    def get_ip_addr(self):
        if self.device:
            address = self.device.shell("ip addr show wlan0")
            find_inet = address.find("inet ")
            last_slash = address.find('/', find_inet)
            ip = address[find_inet+5: last_slash]
            print(ip)
            return ip
        return ""

if __name__ == "__main__":
    logging.getLogger("ppadb").setLevel(logging.DEBUG)

    root = tk.Tk()
    root.title("Android Camera Button")
    root.geometry("320x125+100+100")
    root.resizable(False, False)
    app = CameraButton(master=root)
    app.mainloop()