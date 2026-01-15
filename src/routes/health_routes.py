from flask import Blueprint, jsonify, make_response

health_bp = Blueprint("health_bp", __name__)

@health_bp.route("/api", methods=["GET"])
def api_status():
    return make_response(jsonify({
        "mensagem": "API - OK; Docker - Up"
    }), 200)
