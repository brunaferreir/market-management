from src.config.data_base import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Seller(db.Model):
    __tablename__ = 'sellers'

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(80), nullable=False)
    cnpj = db.Column(db.String(14), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    celular = db.Column(db.String(20), unique=True, nullable=False)

    senha = db.Column(db.String(255), nullable=False)

    status = db.Column(db.String(20), nullable=False, default="inactive")


    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # 🔗 Produtos do seller
    products = db.relationship(
        "Product",
        backref="seller",
        lazy=True,
        cascade="all, delete-orphan"
    )

    # 🔗 Códigos de ativação
    activation_codes = db.relationship(
        'ActivationCode',
        back_populates='seller',
        lazy='dynamic'
    )

    def set_senha(self, senha):
        self.senha = generate_password_hash(senha)

    def check_senha(self, senha):
        return check_password_hash(self.senha, senha)

    def __repr__(self):
        return f'<Seller {self.nome}>'

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cnpj': self.cnpj,
            'email': self.email,
            'celular': self.celular,
            'status': self.status
        }
