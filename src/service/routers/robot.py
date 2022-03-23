import shelve
import os
from flask import Blueprint, request

actionDict = {}
is_in_pi = os.environ.get('IN_PI') is not None
if is_in_pi:
    from pi import manual
    actionDict = {
        'forward': manual.forward,
        'back': manual.back,
        'left': manual.left,
        'right': manual.right,
        'spin_left': manual.spin_left,
        'spin_right': manual.spin_right,
        'stop': manual.stop,
        'beep': manual.beep,
        'fan': manual.fan,
        'camera_up': manual.camera_up,
        'camera_down': manual.camera_down,
        'camera_left': manual.camera_left,
        'camera_right': manual.camera_right,
        'all_servo_init': manual.all_servo_init,
        'all_servo_stop': manual.all_servo_stop,
        'auto_pilot': manual.auto_pilot,
        'stop_auto_pilot': manual.stop_auto_pilot,
        # 'follow_infrared': 
    }

bp = Blueprint('/robot', __name__)


@bp.route('/set/walk_speed/<int:val>', methods=['GET'])
def set_speed(val):
    if is_in_pi:
        manual.set_walk_speed(min(max(1, val), 5))
        return 'set success: ' + str(val)

    return 'ignore: ' + str(val)


@bp.route('/do/<action>', methods=['GET'])
def do(action):
    if action in actionDict:
        actionDict.get(action)()
        return 'success: ' + action

    return 'invalid action: ' + action


# @bp.route('/led/<action>', defaults={'arg': ''})
@bp.route('/led/<int:red>/<int:green>/<int:blue>', methods=['GET'])
def led(red, green, blue):
    red = min(max(0, red), 255)
    green = min(max(0, green), 255)
    blue = min(max(0, blue), 255)

    if is_in_pi:
        manual.set_led_rgb(red, green, blue)
        return ' '.join(['set success:', str(red), str(green), str(blue)])

    return ' '.join(['ignore:', str(red), str(green), str(blue)])
