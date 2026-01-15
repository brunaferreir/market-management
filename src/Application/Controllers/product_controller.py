from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from src.Application.Service.product_service import ProductService


class ProductController:

    @staticmethod
    @jwt_required()
    def create_product():
        seller_id = int(get_jwt_identity())
        data = request.get_json()

        if not data:
            return jsonify({"erro": "Dados inválidos"}), 400

        product = ProductService.create_product(seller_id, data)

        return jsonify({
            "mensagem": "Produto criado com sucesso",
            "produto": product.to_dict()
        }), 201

    @staticmethod
    @jwt_required()
    def get_by_id(id):
        seller_id = int(get_jwt_identity())
        product = ProductService.get_by_id(id, seller_id)

        if not product:
            return jsonify({"error": "Produto não encontrado"}), 404

        return jsonify(product.to_dict()), 200

    @staticmethod
    @jwt_required()
    def list_products():
        seller_id = int(get_jwt_identity())
        products = ProductService.get_products_by_seller(seller_id)

        return jsonify([p.to_dict() for p in products]), 200

    @staticmethod
    @jwt_required()
    def update_product(product_id):
        seller_id = int(get_jwt_identity())
        data = request.get_json()

        product = ProductService.update_product(product_id, seller_id, data)

        if not product:
            return jsonify({"erro": "Produto não encontrado"}), 404

        return jsonify({
            "mensagem": "Produto atualizado",
            "produto": product.to_dict()
        }), 200

    @staticmethod
    @jwt_required()
    def delete_product(product_id):
        seller_id = int(get_jwt_identity())
        success = ProductService.delete_product(product_id, seller_id)

        if not success:
            return jsonify({"erro": "Produto não encontrado"}), 404

        return jsonify({"mensagem": "Produto removido"}), 200
