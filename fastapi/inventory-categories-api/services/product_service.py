from typing import List, Optional
from fastapi import HTTPException

from inventory.schemas.product import (
    Product,
    ProductCreate,
    ProductUpdate,
    ProductListResponse,
    ProductDetailResponse,
)
from inventory.repositories import category_repository
from inventory.repositories import product_repository


class ProductService:

    # list 변환 메서드
    def _to_list_response(self, product: Product) -> ProductListResponse:
        category = category_repository.get_by_id(product.category_id)
        return ProductListResponse(
            id=product.id,
            name=product.name,
            final_price=product.price - product.discount_price,
            category=category.category_name if category else "Unknown",
        )


    # detail 변환 메서드
    def _to_detail_response(self, product: Product) -> ProductDetailResponse:
        category = category_repository.get_by_id(product.category_id)
        return ProductDetailResponse(
            id=product.id,
            name=product.name,
            price=product.price,
            discount_price=product.discount_price,
            final_price=product.price - product.discount_price,
            category=category.category_name if category else "Unknown",
            stock=product.stock,
            is_sold_out=product.stock == 0,  # 0이면 True, 0이 아니면 False
        )


    # 카테고리ID 검증 메서드
    def _get_category_or_404(self, category_id: int):
        category = category_repository.get_by_id(category_id)
        if not category:
            raise HTTPException(status_code=404, detail="해당 카테고리가 존재하지 않습니다.")


    # 상품ID 검증 후 상품 반환 메서드
    def _get_product_or_404(self, product_id: int, category_id: int | None = None):
        product = product_repository.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="상품을 찾을 수 없습니다.")

        if category_id is not None and product.category_id != category_id:
            raise HTTPException(status_code=404, detail="해당 카테고리의 상품이 아닙니다.")

        return product


    # --------------------
    # 상품 생성
    # --------------------
    def create_product(self, category_id: int, data: ProductCreate) -> ProductDetailResponse:
        # 카테고리 존재 여부 확인
        self._get_category_or_404(category_id)

        # discount_price가 price보다 크면 오류
        if data.discount_price > data.price:
            raise HTTPException(
                status_code=400,
                detail="discount_price는 price보다 작아야 합니다."
            )

        # 상품 생성
        product = Product(
            id=None,
            category_id=category_id,
            name=data.name,
            price=data.price,
            discount_price=data.discount_price,
            stock=data.stock
        )

        # 저장
        saved = product_repository.save(product)

        # 응답 변환
        return self._to_detail_response(saved)


    # --------------------
    # 상품 리스트
    # --------------------
    def read_products(
        self,
        keyword: Optional[str] = None,
        category_id: Optional[int] = None,
        limit: int = 20,
    ) -> List[ProductListResponse]:
        products = product_repository.list(keyword, category_id, limit)
        return [self._to_list_response(p) for p in products]


    # --------------------
    # 상품 상세
    # --------------------
    def read_product_by_id(self, product_id: int, category_id: int) -> ProductDetailResponse:
        self._get_category_or_404(category_id)
        product = self._get_product_or_404(product_id, category_id)

        return self._to_detail_response(product)


    # --------------------
    # 상품 수정
    # --------------------
    def update_product(self, product_id: int, data: ProductUpdate, category_id: int) -> ProductDetailResponse:
        self._get_category_or_404(category_id)
        product = self._get_product_or_404(product_id, category_id)

        # 가격 업데이트 및 검증
        # 1. 사용자가 전달한 price가 있으면 적용, 없으면 기존 가격 유지
        new_price = data.price if data.price is not None else product.price

        # 2. 사용자가 전달한 discount_price가 있으면 적용, 없으면 기존 할인 가격 유지
        new_discount = (
            data.discount_price
            if data.discount_price is not None
            else product.discount_price
        )

        # 3. 할인 가격 검증: discount_price는 price보다 클 수 없음
        if new_discount > new_price:
            raise HTTPException(400, "discount_price는 price보다 작아야 합니다.")

        updated = product_repository.update(product, data)
        return self._to_detail_response(updated)


    # --------------------
    # 상품 삭제
    # --------------------
    def delete_product(self, product_id: int, category_id: int) -> None:
        self._get_category_or_404(category_id)
        product = self._get_product_or_404(product_id, category_id)

        product_repository.delete(product.id)


# 싱글톤
product_service = ProductService()
