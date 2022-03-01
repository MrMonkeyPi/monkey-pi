
import shelve
import os
from flask import Blueprint, request

CONFIG_FILE =  os.path.join(os.getcwd(), 'instance', "data", "config")

bp = Blueprint('/setting', __name__)

@bp.route('/', methods=['GET'])
def get_config():
    with shelve.open(CONFIG_FILE) as db:
        return dict(db)

#TODO: no security check here
@bp.route('/', methods=['POST', 'PUT'])
def set_config():
    with shelve.open(CONFIG_FILE) as db:
        # db.update({'video_folders': ['a', 'b', 'c']})
        data = dict(request.get_json())
        db.update(data)
        return dict(db)