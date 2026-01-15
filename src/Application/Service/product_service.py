from src.config.data_base import db
from src.Infrastructure.Model.product import Product


class ProductService:

    @staticmethod
    def create_product(seller_id, data):
        product = Product(
            seller_id=seller_id,
            nome=data.get("nome"),
            preco=data.get("preco"),
            quantidade=data.get("quantidade"),
            status=data.get("status", "ATIVO"),
            imagem=data.get("imagem")
        )

        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def get_products_by_seller(seller_id):
        return Product.query.filter_by(seller_id=seller_id).all()

    @staticmethod
    def get_product_by_id(product_id, seller_id):
        return Product.query.filter_by(
            id=product_id,
            seller_id=seller_id
        ).first()

    # ✅ NOVO: compatível com ProductController.get_by_id(id)
    @staticmethod
    def get_by_id(product_id, seller_id):
        return ProductService.get_product_by_id(product_id, seller_id)

    @staticmethod
    def update_product(product_id, seller_id, data):
        product = ProductService.get_product_by_id(product_id, seller_id)

        if not product:
            return None

        for field in ["nome", "preco", "quantidade", "status", "imagem"]:
            if field in data:
                setattr(product, field, data[field])

        db.session.commit()
        return product

    @staticmethod
    def delete_product(product_id, seller_id):
        product = ProductService.get_product_by_id(product_id, seller_id)

        if not product:
            return False

        db.session.delete(product)
        db.session.commit()
        return True
