from flask import request, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.Application.Service.sale_service import SaleService


class SaleController:

    @staticmethod
    @jwt_required()
    def create_sale():
        seller_id = get_jwt_identity()
        data = request.get_json()

        if not data or "items" not in data:
            return make_response(
                jsonify({"erro": "Itens da venda são obrigatórios"}),
                400
            )

        result = SaleService.create_sale(
            seller_id=seller_id,
            items=data["items"]
        )

        if "error" in result:
            return make_response(jsonify(result), 400)

        return make_response(jsonify(result), 201)

    # 🔹 Lista todas as vendas do seller logado
    @staticmethod
    @jwt_required()
    def get_my_sales():
        seller_id = get_jwt_identity()
        sales = SaleService.get_sales_by_seller(seller_id)

        return jsonify([
            sale.to_dict() for sale in sales
        ]), 200

    # 🔹 Busca venda específica
    @staticmethod
    @jwt_required()
    def get_sale_by_id(sale_id):
        seller_id = get_jwt_identity()
        sale = SaleService.get_sale_by_id(sale_id, seller_id)

        if not sale:
            return make_response(
                jsonify({"erro": "Venda não encontrada"}),
                404
            )

        return jsonify(sale.to_dict()), 200
