import shelve
import os
from flask import Blueprint, request

walkDict = {}
ledDict = {}
is_in_pi = os.environ.get('IN_PI') is not None
if is_in_pi:
    from pi import walk, led
    walkDict = {
        'forward': walk.forward,
        'back': walk.back,
        'left': walk.left,
        'right': walk.right,
        'spin_left': walk.spin_left,
        'spin_right': walk.spin_right,
        'stop': walk.stop
        }
    ledDict = {
        'on': led.on,
        'off': led.off,
        'red': led.red,
        'green': led.green,
        'blue': led.blue,
        'blink': led.blink,
        'loop': led.loop,
    }

bp = Blueprint('/robot', __name__)



@bp.route('/walk/<action>', methods=['GET'])
def walk_(action):
    if action in walkDict:
        walkDict.get(action)()
        return 'success: ' + action
    
    return 'invalid action: ' + action

# @bp.route('/led/<action>', defaults={'arg': ''})
@bp.route('/led/<action>/<arg>', methods=['GET'])
def led_(action, arg):
    if action in ledDict:
        ledDict.get(action)(arg)
        return 'success: ' + action
    
    return 'invalid action: ' + action