import os
from pickle import TRUE
from threading import Timer
from flask import Blueprint, request

is_in_pi = os.environ.get('IN_PI') is not None
if is_in_pi:
    from pi import manual

bp = Blueprint('/status', __name__)

is_initlized = False


@bp.route('/')
def health():
    return "alive"


@bp.route('/init')
def init():
    global is_initlized

    if is_initlized or not is_in_pi:
        return "already initilized"

    is_initlized = True
    manual.init()
    manual.all_servo_init()
    return "initilized"


@bp.route('/shutdown')
def shutdown():
    t = Timer(1.0, quit_process)
    t.start()
    return "will shutdown Monkey server in next second"


def quit_process():
    manual.clean()
    os._exit(0)
