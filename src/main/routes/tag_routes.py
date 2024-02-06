from flask import Blueprint, request, jsonify

tag_routes_bp = Blueprint('tags_routes', __name__)

@tag_routes_bp.route('/create_tag', methods=['POST'])
def create_tagg():
    print(request.json)
    return jsonify({"resp": "ok"}), 200
