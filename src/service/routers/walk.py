import shelve
import os
from flask import Blueprint, request

actionDict = {}
is_in_local = os.environ.get('IN_LOCAL') is not None
if is_in_local: 
    from robot import walk 
    actionDict = {
        'forward': walk.forward,
        'back': walk.back,
        'left': walk.left,
        'right': walk.right,
        'spin_left': walk.spin_left,
        'spin_right': walk.spin_right,
        'stop': walk.stop
        }

bp = Blueprint('/walk', __name__)



@bp.route('/a/<action>', methods=['GET'])
def walk(action):
    if action in actionDict:
        actionDict.get(action)()
        return {'status': 'success', 'message': action }
    
    return {'status': 'failed', 'message': 'invalid action: '+ action }
