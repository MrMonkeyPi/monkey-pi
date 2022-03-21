import shelve
import os
from flask import Blueprint, request

is_in_local = os.environ.get('IN_LOCAL') is not None
if is_in_local: 
    from robot import walk 

bp = Blueprint('/walk', __name__)

@bp.route('/forward', methods=['GET'])
def forward():
    
    return {'status': 'success', 'message': 'forward'}


@bp.route('/backward', methods=['GET'])
def backward():
    return {'status': 'success', 'message': 'backward'}