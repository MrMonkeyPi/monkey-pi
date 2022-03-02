import os
from threading import Timer
from flask import Blueprint, request



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
    os._exit(0)
