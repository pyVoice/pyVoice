#!/bin/bash

echo "Setup pyAudio..."
sudo apt install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0

echo "Setup Python 3.9 dev..."
sudo apt install python3.9-dev

echo "Setup PIP packages"
pip install -U setuptools wheel
pip install vext
pip install vext.gi

echo "Setup cairo..."
sudo apt-get install libcairo2-dev

echo "Setup random stuff..."
sudo apt install libgirepository1.0-dev
sudo apt install python3-gst-1.0

echo "Setup PyGObject"
pip install PyGObject