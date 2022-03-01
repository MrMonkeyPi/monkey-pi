import shelve
from flask import Blueprint, request



bp = Blueprint('/walk', __name__)

@bp.route('/forward', methods=['GET'])
def forward():
    return {'status': 'success', 'message': 'forward'}


@bp.route('/backward', methods=['GET'])
def backward():
    return {'status': 'success', 'message': 'backward'}