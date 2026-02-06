from typing import List, Optional
from product.schemas.product import Product, ProductUpdate


class ProductRepository:
    def __init__(self):
        # 임시 DB
        self.products: List[Product] = []
        self._id_counter = 0

    # -------------------------------
    # 상품 생성
    # -------------------------------
    def save(self, new_product: Product):
        # <-- db를 사용하면 없어질 로직
        self._id_counter += 1
        new_product.id = self._id_counter
        # -->
        self.products.append(new_product)
        return new_product
    
    # -------------------------------
    # 전체 상품 조회 (옵션 필터)
    # -------------------------------
    def list(
        self,
        keyword: Optional[str] = None,
        category: Optional[str] = None,
        limit: int = 20
    ) -> List[Product]:
        result = self.products

        if keyword:
            result = [p for p in result if keyword.lower() in p.name.lower()]
        if category:
            result = [p for p in result if p.category.lower() == category.lower()]

        return result[:limit]

    # -------------------------------
    # ID로 상품 조회
    # -------------------------------
    def get_by_id(self, product_id: int) -> Optional[Product]:
        return next((p for p in self.products if p.id == product_id), None)

    # -------------------------------
    # 상품 수정
    # -------------------------------
    def update(self, product: Product, data: ProductUpdate) -> Product:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(product, key, value)
        return product

    # -------------------------------
    # 상품 삭제
    # -------------------------------
    def delete(self, product_id: int) -> bool:
        for i, p in enumerate(self.products):
            if p.id == product_id:
                self.products.pop(i)
                return True
        return False

# Repository 싱글톤
product_repository = ProductRepository()
