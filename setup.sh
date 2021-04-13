#!/bin/bash
sudo mkdir /opt/wallpaperchecker/
sudo cp wallpaperchecker.py /opt/wallpaperchecker/

if ! command -v python3
then
	echo "Please install python3"
	exit
fi

if ! command -v pip3
then
	echo "Please install python3 pip"
	exit
fi

pip3 install -r requirements.txt
