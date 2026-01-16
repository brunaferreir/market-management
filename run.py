from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from src.config.data_base import init_db, db
from src.routes.auth_routes import auth_bp
from src.routes.seller_routes import seller_bp
from src.routes.health_routes import health_bp
from src.routes.product_routes import product_bp
from src.routes.sale_routes import sale_bp

def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    app.config["JWT_SECRET_KEY"] = "obsidian"

    CORS(
        app,
        resources={r"/api/*": {"origins": "*"}},
        supports_credentials=True
    )

    JWTManager(app)
    init_db(app)

    app.register_blueprint(health_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(seller_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(sale_bp)

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
