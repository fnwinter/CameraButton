#!/bin/bash
pushd ./source
pyinstaller --icon=./camera.ico --onefile --noconsole ./CameraButton.py
popd