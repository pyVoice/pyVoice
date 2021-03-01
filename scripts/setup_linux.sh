#!/bin/bash

echo "\n\n Setup pyAudio... \n\n"
sudo apt install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0

echo "\n\n Setup Python 3.9 dev... \n\n"
sudo apt install python3.9-dev

echo "\n\n Setup PIP packages \n\n"
pip install -U setuptools wheel
pip install vext
pip install vext.gi