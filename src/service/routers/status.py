import os
from threading import Timer
from flask import Blueprint, request

is_in_local = os.environ.get('IN_LOCAL') is not None
if is_in_local: 
    from robot import walk 
    walk.motor_init()


bp = Blueprint('/status', __name__)

@bp.route('/')
def health():
    return "alive"


@bp.route('/shutdown')
def shutdown():
    t = Timer(1.0, quit_process)
    t.start()
    return "will shutdown Monkey server in next second"


def quit_process():
    walk.motor_clean()
    os._exit(0)
