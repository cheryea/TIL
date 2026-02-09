from typing import Annotated
from fastapi import APIRouter, Path, Query, status

from inventory.schemas.product import (
    ProductCreate,
    ProductDetailResponse,
    ProductListResponse,
    ProductUpdate,
)
from inventory.services.product_service import product_service

# -----------------------------
# Product Router
# -----------------------------
# 모든 경로는 "카테고리 기준"으로 동작
# URL 구조: /{category_id}/products/...
# tags=["products"]로 Swagger 그룹 지정
router = APIRouter(prefix="/categories/{category_id}/products", tags=["products"])


# -----------------------------
# 상품 등록
# -----------------------------
# POST /{category_id}/products
@router.post("", response_model=ProductDetailResponse, status_code=status.HTTP_201_CREATED)
def create_product(
    category_id: Annotated[int, Path(ge=1, description="카테고리 고유 번호")],
    data: ProductCreate
):
    """
    Path 검증: category_id >= 1
    Body 검증: ProductCreate (name, price, discount_price, stock)
    """

    return product_service.create_product(category_id, data)


# -----------------------------
# 상품 리스트 조회
# -----------------------------
# GET /{category_id}/products\
@router.get("", response_model=list[ProductListResponse])
def read_products(
    category_id: Annotated[int, Path(ge=1, description="카테고리 고유 번호")],
    keyword: Annotated[str | None, Query(min_length=2, description="검색 키워드")] = None,
    limit: Annotated[int | None, Query(le=100, description="조회 개수 제한")] = 20,
):
    """
    Path 검증: category_id >= 1
    Query Params:
    - keyword: 선택, 상품명 검색, 최소 2자
    - limit: 선택, 최대 100개
    """

    return product_service.read_products(keyword, category_id, limit)


# -----------------------------
# 상품 상세 조회
# -----------------------------
# GET /{category_id}/products/{product_id}
@router.get("/{product_id}", response_model=ProductDetailResponse)
def read_product_by_id(
    category_id: Annotated[int, Path(ge=1, description="카테고리 고유 번호")],
    product_id: Annotated[int, Path(ge=1, description="상품 고유 번호")]
):
    """
    Path 검증: category_id, product_id >= 1
    """
    return product_service.read_product_by_id(product_id, category_id)


# -----------------------------
# 상품 수정
# -----------------------------
# PUT /{category_id}/products/{product_id}
@router.put("/{product_id}", response_model=ProductDetailResponse)
def update_product(
    category_id: Annotated[int, Path(ge=1, description="카테고리 고유 번호")],
    product_id: Annotated[int, Path(ge=1, description="상품 고유 번호")],
    data: ProductUpdate
):
    """
    Path 검증: category_id, product_id >= 1
    Body 검증: ProductUpdate (선택 필드)
    """

    return product_service.update_product(product_id, data, category_id)


# -----------------------------
# 상품 삭제
# -----------------------------
# DELETE /{category_id}/products/{product_id}
@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    category_id: Annotated[int, Path(ge=1, description="카테고리 고유 번호")],
    product_id: Annotated[int, Path(ge=1, description="상품 고유 번호")],
):
    """
    Path 검증: category_id, product_id >= 1
    """

    product_service.delete_product(product_id, category_id)
