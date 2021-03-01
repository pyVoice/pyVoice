#!/bin/bash

echo "Setup pyAudio..."
sudo apt install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0

echo "Setup Python 3.9 dev..."
sudo apt install python3.9-dev

echo "Setup Vext and Gi"
pip install -U setuptools wheel
pip install vext
pip install vext.gi