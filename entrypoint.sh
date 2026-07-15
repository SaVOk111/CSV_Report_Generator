#!/bin/bash

set -e
Xvfb :99 -screen 0 1600x900x24 &

export DISPLAY=:99

x11vnc -display :99 -nopw -forever -shared -quiet &

websockify --web=/usr/share/novnc/ 6080 localhost:5900 &

sleep 2

exec python src/main.py