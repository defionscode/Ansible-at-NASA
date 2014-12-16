# Copyright (c) 2014, Matt Makai
# All rights reserved.
# Full License can be read here: http://bit.ly/1qBgqzn

from flask.ext.socketio import emit

from . import socketio


@socketio.on('connect', namespace='/nasa')
def test_connect():
    pass

@socketio.on('disconnect', namespace='/nasa')
def test_disconnect():
    pass

