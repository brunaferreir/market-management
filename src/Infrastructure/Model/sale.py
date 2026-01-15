from src.config.data_base import db
from datetime import datetime


class Sale(db.Model):
    __tablename__ = "sales"

    id = db.Column(db.Integer, primary_key=True)

    seller_id = db.Column(
        db.Integer,
        db.ForeignKey("sellers.id"),
        nullable=False
    )

    total_value = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="FINALIZADA")

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # 🔗 Relacionamentos
    seller = db.relationship(
        "Seller",
        backref=db.backref("sales", lazy=True)
    )

    items = db.relationship(
        "SaleItem",
        back_populates="sale",
        cascade="all, delete-orphan",
        lazy=True
    )

    def __repr__(self):
        return f"<Sale id={self.id} seller_id={self.seller_id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "seller_id": self.seller_id,
            "total_value": self.total_value,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "items": [item.to_dict() for item in self.items]
        }
