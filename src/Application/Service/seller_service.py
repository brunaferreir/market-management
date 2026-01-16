import random
from src.Infrastructure.Model.seller import Seller
from src.Infrastructure.Model.activation_code import ActivationCode
from src.config.data_base import db, bcrypt
from src.Infrastructure.http.whats_app import enviar_codigo_whatsapp
from flask_jwt_extended import create_access_token


from werkzeug.security import check_password_hash



class SellerService:

    # =========================
    # LOGIN
    # =========================
    @staticmethod
    def login_seller(email, senha):
        seller = Seller.query.filter_by(email=email).first()

        if not seller:
            return {"error": "Credenciais inválidas"}, 401

        if not bcrypt.check_password_hash(seller.senha, senha):
            return {"error": "Credenciais inválidas"}, 401

        if seller.status != "active":
            return {"error": "Seller inativo"}, 403

        token = create_access_token(identity=str(seller.id))

        return {
            "token": token,
            "seller": seller.to_dict()
        }, 200
    


    # =========================
    # CRIAR SELLER
    # =========================
    @staticmethod
    def create_seller(nome, cnpj, email, celular, senha):
        # 🔎 Verifica se CNPJ já existe
        if db.session.query(Seller).filter_by(cnpj=cnpj).first():
            return {"error": "CNPJ já cadastrado"}, 409

        # 🔎 Verifica se email já existe
        if db.session.query(Seller).filter_by(email=email).first():
            return {"error": "Email já cadastrado"}, 409

        hashed_password = bcrypt.generate_password_hash(senha).decode("utf-8")

        seller = Seller(
            nome=nome,
            cnpj=cnpj,
            email=email,
            celular=celular,
            senha=hashed_password,
            status="inactive"
        )

        db.session.add(seller)
        db.session.commit()

        # 🔐 Gera código de ativação
        codigo = str(random.randint(1000, 9999))

        # 📲 Envio do WhatsApp (NÃO pode derrubar a API)
        try:
            enviar_codigo_whatsapp(celular, codigo)
        except Exception as e:
            print("Erro ao enviar WhatsApp:", e)
            # Continua o fluxo mesmo se falhar

        activation = ActivationCode(
            codigo=codigo,
            seller_id=seller.id  # ⚠️ seller_id (não user_id)
        )

        db.session.add(activation)
        db.session.commit()

        return {
            "message": "Seller cadastrado com sucesso. Código de ativação enviado."
        }, 201




    # =========================
    # ATIVAR SELLER
    # =========================
    @staticmethod
    def activate_seller(celular, codigo):
        seller = Seller.query.filter_by(celular=celular).first()
        if not seller:
            return {"error": "Seller não encontrado"}, 404

        activation = ActivationCode.query.filter_by(
            seller_id=seller.id,
            codigo=codigo,
            used=False
        ).first()

        if not activation:
            return {"error": "Código inválido ou já utilizado"}, 400

        activation.used = True
        seller.status = "active"

        db.session.commit()

        return {"message": "Seller ativado com sucesso"}, 200

    # =========================
    # GET BY ID
    # =========================
    @staticmethod
    def get_by_id(seller_id):
        return Seller.query.get(seller_id)

    # =========================
    # UPDATE
    # =========================
    @staticmethod
    def update(seller_id, data):
        seller = Seller.query.get(seller_id)
        if not seller:
            return None

        if "senha" in data:
            data["senha"] = bcrypt.generate_password_hash(
                data["senha"]
            ).decode("utf-8")

        for key, value in data.items():
            setattr(seller, key, value)

        db.session.commit()
        return seller

    # =========================
    # INATIVAR
    # =========================
    @staticmethod
    def inactivate(seller_id):
        seller = Seller.query.get(seller_id)
        if not seller:
            return None

        seller.status = "inactive"
        db.session.commit()
        return seller

    # =========================
    # DELETE
    # =========================
    @staticmethod
    def delete(seller_id):
        seller = Seller.query.get(seller_id)
        if not seller:
            return False

        ActivationCode.query.filter_by(
            seller_id=seller.id
        ).delete()

        db.session.delete(seller)
        db.session.commit()
        return True
