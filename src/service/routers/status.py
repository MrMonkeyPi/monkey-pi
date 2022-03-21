import os
from threading import Timer
from flask import Blueprint, request

is_in_pi = os.environ.get('IN_PI') is not None
if is_in_pi:
    from pi import walk, led
    walk.motor_init()
    led.init()
    led.loop()


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
