from flask import request, jsonify, make_response
from flask_jwt_extended import get_jwt_identity, jwt_required
from src.Application.Service.seller_service import SellerService

class AuthController:

    @staticmethod
    def login():
        data = request.get_json()
        if not data:
            return make_response(jsonify({"erro": "JSON inválido"}), 400)

        email = data.get("email")
        senha = data.get("senha")
        if not email or not senha:
            return make_response(jsonify({"erro": "Email e senha são obrigatórios"}), 400)

        # ✅ usa o método que já existe
        response, status = SellerService.login_seller(email, senha)
        return jsonify(response), status

    @staticmethod
    @jwt_required()
    def me():
        seller_id = int(get_jwt_identity())
        seller = SellerService.get_by_id(seller_id)

        if not seller:
            return jsonify({"erro": "Seller não encontrado"}), 404

        return jsonify(seller.to_dict()), 200
