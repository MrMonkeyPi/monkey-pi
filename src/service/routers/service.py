
import shelve
import os
from flask import Blueprint, request, jsonify

from pi.audio import say, sing

APP_SETTING_FILE = os.path.join(os.getcwd(), 'instance', "data", "app")

bp = Blueprint('/service', __name__)


@bp.route('/rules', methods=['GET'])
def get_rules():
    with shelve.open(APP_SETTING_FILE) as db:
        try:
            return jsonify(dict(db)['SERVICE_RULES'])
        except:
            return jsonify([])


@bp.route('/rules', methods=['POST'])
def set_rules():
    try:
        with shelve.open(APP_SETTING_FILE) as db:
            data = list(request.get_json())
            db.update({'SERVICE_RULES': data})
            return 'success'
    except:
        return 'failed'


@bp.route('/rules/execute/<int:key>', methods=['GET'])
def execute_rule(key):
    item = None
    rscDirs = []
    with shelve.open(APP_SETTING_FILE) as db:
        try:
            dbDic = dict(db)
            item = dbDic['SERVICE_RULES'][key]
            rscDirs = dbDic['MEDIA_HOME']
        except:
            pass

    if item is None or item['rule'] is None or len(rscDirs) < 1:
        return 'invalid rule'

    if item['rule'].startswith('sing '):
        name = item['rule'][5:]
        sing(name, rscDirs)
        return ' '.join(['success:', 'sing', name])
    elif item['rule'].startswith('say '):
        line = item['rule'][4:]
        say(line)
        return ' '.join(['success:', 'say', line])
    
    return 'ignore'
