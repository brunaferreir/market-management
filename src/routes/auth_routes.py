from flask import Blueprint
from src.Application.Controllers.auth_controller import AuthController

auth_bp = Blueprint("auth_bp", __name__, url_prefix="/api/auth")

auth_bp.route("/login", methods=["POST"])(AuthController.login)
auth_bp.route("/me", methods=["GET"])(AuthController.me)
