from src.config.data_base import db
from sqlalchemy.orm import relationship

class ActivationCode(db.Model):
    __tablename__ = 'activation_codes'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(6), nullable=False)
    used = db.Column(db.Boolean, default=False)

    seller_id = db.Column(
        db.Integer,
        db.ForeignKey('sellers.id'),
        nullable=False
    )

    seller = db.relationship(
        'Seller',
        back_populates='activation_codes'
    )

