import tkinter as tk

from ppadb.client import Client as AdbClient

class CameraButton(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.columnconfigure(0, weight = 1)
        self.remote_connection = tk.IntVar()
        self.create_widgets()

    def create_widgets(self):
        self.connectButton = tk.Button(self)
        self.connectButton["text"] = "Connect"
        self.connectButton["command"] = self.connection
        self.connectButton.grid(row=0, column=0, sticky = tk.W + tk.E, columnspan=2)

        self.remoteCheckButton = tk.Checkbutton(self, variable=self.remote_connection)
        self.remoteCheckButton["text"] = "Remote connection"
        self.remoteCheckButton.grid(row=0, column=2)

        self.captureButton = tk.Button(self)
        self.captureButton["text"] = "Capture"
        self.captureButton["command"] = self.capture
        self.captureButton.grid(row=1, column=0, columnspan=3, sticky = tk.W + tk.E)

        self.label = tk.Label(self, text = "Time button (Tick:sec)", width=30)
        self.label.grid(row=2, column=0, sticky = tk.W + tk.E, columnspan=3)

        self.timeEntry = tk.Entry(self)
        self.timeEntry.insert(0,'3')
        self.timeEntry.grid(row=3, column=0, sticky = tk.W + tk.E + tk.N + tk.S)

        self.startButton = tk.Button(self, width=10)
        self.startButton["text"] = "Start"
        self.startButton["command"] = self.start
        self.startButton.grid(row=3, column=1, sticky = tk.W + tk.E)

        self.stopButton = tk.Button(self, width=10)
        self.stopButton["text"] = "Stop"
        self.stopButton["command"] = self.stop
        self.stopButton.grid(row=3, column=2, sticky = tk.W + tk.E)

    def connection(self):
        print("connect")
        print(self.remote_connection.get())

    def capture(self):
        print("capture")

    def start(self):
        print("start")

    def stop(self):
        print("stop")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Android Camera Button")
    root.geometry("320x100+100+100")
    root.resizable(False, False)
    app = CameraButton(master=root)
    app.mainloop()