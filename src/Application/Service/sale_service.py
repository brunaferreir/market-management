from src.config.data_base import db
from src.Infrastructure.Model.sale import Sale
from src.Infrastructure.Model.sale_item import SaleItem
from src.Infrastructure.Model.product import Product
from src.Infrastructure.Model.seller import Seller


class SaleService:

    @staticmethod
    def create_sale(seller_id, items):
        """
        items = [
            { "product_id": 1, "quantity": 2 },
            { "product_id": 3, "quantity": 1 }
        ]
        """

        # 1️⃣ Verifica seller
        seller = db.session.get(Seller, seller_id)
        if not seller:
            return {"error": "Seller não encontrado"}

        if seller.status.lower() != "active":
            return {"error": "Seller inativo"}

        total_value = 0
        sale_items = []

        # 2️⃣ Valida produtos e estoque
        for item in items:
            product = db.session.get(Product, item["product_id"])

            if not product:
                return {"error": f"Produto {item['product_id']} não encontrado"}

            if product.status.lower() != "ativo":
                return {"error": f"Produto {product.nome} inativo"}

            if product.quantidade < item["quantity"]:
                return {"error": f"Estoque insuficiente para {product.nome}"}

            subtotal = product.preco * item["quantity"]
            total_value += subtotal

            sale_items.append({
                "product": product,
                "quantity": item["quantity"],
                "unit_price": product.preco,
                "subtotal": subtotal
            })

        # 3️⃣ Cria venda
        sale = Sale(
            seller_id=seller.id,
            total_value=total_value,
            status="FINALIZADA"
        )

        db.session.add(sale)
        db.session.flush()  # 🔥 Gera o ID da venda

        # 4️⃣ Cria itens da venda + baixa estoque
        for item in sale_items:
            sale_item = SaleItem(
                sale_id=sale.id,
                product_id=item["product"].id,
                quantity=item["quantity"],
                unit_price=item["unit_price"],
                subtotal=item["subtotal"]
            )

            product = item["product"]
            product.quantidade -= item["quantity"]

            if product.quantidade <= 0:
                product.quantidade = 0
                product.status = "INATIVO"

            db.session.add(sale_item)


            # item["product"].quantidade -= item["quantity"]
            # db.session.add(sale_item)

        db.session.commit()

        return {
            "message": "Venda realizada com sucesso",
            "sale": sale.to_dict()
        }
    
    @staticmethod
    def list_sales_by_seller(seller_id):
     sales = Sale.query.filter_by(seller_id=seller_id).order_by(Sale.created_at.desc()).all()

     return {
            "total": len(sales),
            "sales": [sale.to_dict() for sale in sales]
        }