from flask import request, jsonify, make_response
from flask_jwt_extended import ( create_access_token,get_jwt_identity,
jwt_required
)


from src.Application.Service.seller_service import SellerService




class SellerController:

    # -------------------- CADASTRO SELLER
    @staticmethod
    def create_seller():
        data = request.get_json()
        if not data:
            return make_response(jsonify({"erro": "Dados inválidos"}), 400)

        result = SellerService.create_seller(
            data.get("nome"),
            data.get("cnpj"),
            data.get("email"),
            data.get("celular"),
            data.get("senha")
        )
        return jsonify(result), 201

    # -------------------- ATIVA SELLER
    @staticmethod
    def activate_seller():
        data = request.get_json()
        if not data:
            return make_response(jsonify({"erro": "Dados inválidos"}), 400)

        result = SellerService.activate_seller(
            data.get("celular"),
            data.get("codigo")
        )
        return jsonify(result), 200



    # -------------------- LOGIN (OBRIGATÓRIO PARA AUTH)


    @staticmethod
    def login_seller():
        data = request.get_json()
        if not data:
            return make_response(jsonify({"erro": "Dados inválidos"}), 400)

        email = data.get("email")
        senha = data.get("senha")

        if not email or not senha:
            return make_response(
                jsonify({"erro": "Email e senha são obrigatórios"}), 
                400
            )

        # 🔥 CORREÇÃO PRINCIPAL AQUI
        response, status = SellerService.login_seller(email, senha)

        return jsonify(response), status


    # -------------------- DADOS DO SELLER LOGADO
    @staticmethod
    @jwt_required()
    def get_me():
        seller_id = get_jwt_identity()
        seller = SellerService.get_seller_by_id(seller_id)

        if not seller:
            return make_response(jsonify({"erro": "Seller não encontrado"}), 404)

        return jsonify(seller.to_dict()), 200

    # -------------------- BUSCAR SELLER POR ID
    @staticmethod
    def get_seller_by_id(seller_id):
        seller = SellerService.get_seller_by_id(seller_id)

        if not seller:
            return make_response(jsonify({"erro": "Seller não encontrado"}), 404)

        return jsonify(seller.to_dict()), 200

    # -------------------- ATUALIZAR SELLER
    @staticmethod
    def update_seller(seller_id):
        data = request.get_json()
        if not data:
            return make_response(jsonify({"erro": "Nenhum dado para atualizar"}), 400)

        seller = SellerService.update_seller(seller_id, data)
        if not seller:
            return make_response(jsonify({"erro": "Seller não encontrado"}), 404)

        return jsonify({
            "mensagem": "Seller atualizado com sucesso",
            "seller": seller.to_dict()
        }), 200

    # -------------------- INATIVAR SELLER
    @staticmethod
    def inactivate_seller(seller_id):
        seller = SellerService.inactivate_seller(seller_id)

        if not seller:
            return make_response(jsonify({"erro": "Seller não encontrado"}), 404)

        return jsonify({
            "mensagem": "Seller inativado com sucesso",
            "seller": seller.to_dict()
        }), 200

    # -------------------- DELETAR SELLER
    @staticmethod
    def delete_seller(seller_id):
        success = SellerService.delete_seller(seller_id)

        if not success:
            return make_response(jsonify({"erro": "Seller não encontrado"}), 404)

        return jsonify({"mensagem": "Seller removido com sucesso"}), 200
