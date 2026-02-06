from typing import List, Optional
from fastapi import HTTPException

from product.schemas.product import (
    Product,
    ProductCreate,
    ProductUpdate,
    ProductListResponse,
    ProductDetailResponse,
)
from product.repositories.product_repository import product_repository


class ProductService:

    # 🔹 변환 메서드
    def _to_list_response(self, product: Product) -> ProductListResponse:
        return ProductListResponse(
            id=product.id,
            name=product.name,
            final_price=product.price - product.discount_price,
            category=product.category,
        )

    def _to_detail_response(self, product: Product) -> ProductDetailResponse:
        return ProductDetailResponse(
            id=product.id,
            name=product.name,
            final_price=product.price - product.discount_price,
            category=product.category,
            stock=product.stock,
            is_sold_out=product.stock == 0,
        )

    # --------------------
    # 상품 생성
    # --------------------
    def create_product(self, data: ProductCreate) -> ProductDetailResponse:
        # Pydantic(ProductCreate)로 body 검증 완료
        product = Product(
            id=None,
            name=data.name,
            price=data.price,
            discount_price=data.discount_price,
            stock=data.stock,
            category=data.category,
        )
        saved = product_repository.save(product)
        return self._to_detail_response(saved)

    # --------------------
    # 상품 리스트
    # --------------------
    def read_products(
        self,
        keyword: Optional[str] = None,
        category: Optional[str] = None,
        limit: int = 20,
    ) -> List[ProductListResponse]:
        products = product_repository.list(keyword, category, limit)
        return [self._to_list_response(p) for p in products]

    # --------------------
    # 상품 상세
    # --------------------
    def read_product_by_id(self, product_id: int) -> ProductDetailResponse:
        product = product_repository.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="상품을 찾을 수 없습니다.")
        return self._to_detail_response(product)

    # --------------------
    # 상품 수정
    # --------------------
    def update_product(
        self, product_id: int, data: ProductUpdate
    ) -> ProductDetailResponse:
        product = product_repository.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="상품을 찾을 수 없습니다.")

        updated = product_repository.update(product, data)
        return self._to_detail_response(updated)

    # --------------------
    # 상품 삭제
    # --------------------
    def delete_product(self, product_id: int) -> None:
        if not product_repository.delete(product_id):
            raise HTTPException(status_code=404, detail="상품을 찾을 수 없습니다.")

# 싱글톤
product_service = ProductService()
