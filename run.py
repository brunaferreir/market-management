from flask import Flask
from flask_jwt_extended import JWTManager

from src.config.data_base import init_db, db

from src.routes.auth_routes import auth_bp
from src.routes.seller_routes import seller_bp
from src.routes.health_routes import health_bp
from src.routes.product_routes import product_bp
from src.routes.sale_routes import sale_bp

# 🔹 MODELS (IMPORTANTE PARA db.create_all)
from src.Infrastructure.Model.seller import Seller
from src.Infrastructure.Model.product import Product
from src.Infrastructure.Model.activation_code import ActivationCode
from src.Infrastructure.Model.sale import Sale          # 👈 FALTAVA
from src.Infrastructure.Model.sale_item import SaleItem # 👈 FALTAVA


def create_app():
    app = Flask(__name__)

    # Configurações
    app.config["JWT_SECRET_KEY"] = "obsidian"

    # Extensões
    JWTManager(app)
    init_db(app)

    # Blueprints
    app.register_blueprint(health_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(seller_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(sale_bp)

    # Cria tabelas
    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
