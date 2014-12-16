# Copyright (c) 2014, Matt Makai
# All rights reserved.
# Full License can be read here: http://bit.ly/1qBgqzn

from gevent import monkey
monkey.patch_all()

import os
import redis

from nasa import app, redis_db, socketio
from flask.ext.script import Manager, Shell

manager = Manager(app)

def make_shell_context():
    return dict(app=app, redis_db=redis_db)

manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def runserver():
    socketio.run(app, "0.0.0.0", port=5001)

@manager.command
def clear_redis():
    redis_cli = redis.StrictRedis(host='localhost', port='6379', db='0')
    redis_cli.delete('noob')
    redis_cli.delete('some')
    redis_cli.delete('great')

if __name__ == '__main__':
    manager.run()

