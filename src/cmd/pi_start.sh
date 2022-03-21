#!/bin/sh

sleep 60

cd ~/monkey-pi/src/service

export MEDIA_HOME=/some/media/root1/:/some/media/root2/ && export IN_PI=TRUE && python3 setup.py
python3 app.py &