from src.config.data_base import db
from datetime import datetime


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    seller_id = db.Column(
        db.Integer,
        db.ForeignKey("sellers.id"),
        nullable=False
    )

    nome = db.Column(db.String(120), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default="ATIVO")
    imagem = db.Column(db.String(255))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco,
            "quantidade": self.quantidade,
            "status": self.status,
            "imagem": self.imagem,
            "created_at": self.created_at.isoformat()
        }
