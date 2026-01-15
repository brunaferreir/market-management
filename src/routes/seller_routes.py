from flask import Blueprint
from src.Application.Controllers.seller_controller import SellerController
from flask_jwt_extended import jwt_required

seller_bp = Blueprint("seller_bp", __name__, url_prefix="/api/sellers")


@seller_bp.route("", methods=["POST"])
def create_seller():
    return SellerController.create_seller()


@seller_bp.route("/activate", methods=["POST"])
def activate_seller():
    return SellerController.activate_seller()


@seller_bp.route("/<int:user_id>", methods=["GET"])
@jwt_required()
def get_seller(user_id):
    return SellerController.get_seller_by_id(user_id)


@seller_bp.route("/<int:user_id>", methods=["PUT"])
@jwt_required()
def update_seller(user_id):
    return SellerController.update_seller(user_id)


@seller_bp.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_seller(user_id):
    return SellerController.delete_seller(user_id)


@seller_bp.route("/<int:user_id>/status", methods=["PATCH"])
@jwt_required()
def inactivate_seller(user_id):
    return SellerController.inactivate_seller(user_id)