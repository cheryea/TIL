# inventory/repositories/__init__.py
from .category_repository import category_repository
from .product_repository import product_repository

__all__ = ["category_repository", "product_repository"]
