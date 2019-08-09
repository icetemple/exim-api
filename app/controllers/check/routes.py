from flask import request, jsonify

from .blueprint import controller as check
from app.helpers.exim import check_delivery_route


@check.route('/route/', methods=['POST'])
def delivery_route():
    json = request.get_json()
    email = json.get('email', '').strip()
    if not email:
        return jsonify(error='Email is required'), 422

    stdout, stderr = check_delivery_route(email)
    if 'host lookup did not complete' in stdout:
        return jsonify(error='Host cannot be resolved')

    return jsonify(success=True)
