from flask import Blueprint
from src.Application.Controllers.product_controller import ProductController

product_bp = Blueprint(
    "product_bp",
    __name__,
    url_prefix="/api/products"
)

product_bp.add_url_rule(
    "",
    view_func=ProductController.create_product,
    methods=["POST"],
    endpoint="create_product"
)


product_bp.add_url_rule(
    "/<int:id>",
    view_func=ProductController.get_by_id,
    methods=["GET"],
    endpoint="get_by_id"
)

product_bp.add_url_rule(
    "",
    view_func=ProductController.list_products,
    methods=["GET"],
    endpoint="list_products"
)

product_bp.add_url_rule(
    "/<int:product_id>",
    view_func=ProductController.update_product,
    methods=["PUT"],
    endpoint="update_product"
)

product_bp.add_url_rule(
    "/<int:product_id>",
    view_func=ProductController.delete_product,
    methods=["DELETE"],
    endpoint="delete_product"
)
