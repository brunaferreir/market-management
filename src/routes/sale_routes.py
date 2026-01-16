from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.Application.Service.sale_service import SaleService

sale_bp = Blueprint("sale_bp", __name__, url_prefix="/api/sales")

# =========================
# POST /api/sales
# =========================
@sale_bp.route("", methods=["POST"])
@jwt_required()
def create_sale():
    data = request.get_json()

    if not data or "items" not in data:
        return jsonify({"error": "Itens da venda são obrigatórios"}), 400

    seller_id = int(get_jwt_identity())
    items = data["items"]

    result = SaleService.create_sale(seller_id, items)

    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 400

    return jsonify(result), 201


# =========================
# GET /api/sales
# =========================
@sale_bp.route("", methods=["GET"])
@jwt_required()
def list_sales():
    seller_id = int(get_jwt_identity())
    result = SaleService.list_sales_by_seller(seller_id)
    return jsonify(result), 200
