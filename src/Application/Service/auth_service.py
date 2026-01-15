from flask_jwt_extended import create_access_token
from src.Infrastructure.Model.seller import User
from src.config.data_base import bcrypt


class AuthService:

    @staticmethod
    def login(email, senha):
        seller = User.query.filter_by(email=email).first()

        if not seller:
            return {"error": "Credenciais inválidas"}

        if seller.status != "active":
            return {"error": "Seller inativo"}

        if not bcrypt.check_password_hash(seller.password, senha):
            return {"error": "Credenciais inválidas"}

        token = create_access_token(identity=seller.id)
        return {"token": token}
