from product.schemas.product import ProductCreate, ProductDetailResponse, ProductListResponse, ProductUpdate
from product.services.product_service import product_service

from typing import Annotated
from fastapi import APIRouter, status, Path, Query

router = APIRouter(prefix="/products", tags=["products"])



# 상품 등록
# 검증 : Body 검증 (data: ProductCreate)
@router.post("", response_model=ProductDetailResponse, status_code=status.HTTP_201_CREATED)
def create_product(data: ProductCreate):
    return product_service.create_product(data)


# 상품 리스트
# - **파라미터 (Query)**:
#     - `keyword`: 선택, 최소 2자 이상
#     - `p-category`: 선택 (alias 적용)
#     - `limit`: 선택, 최대 100개 (기본값 20)
@router.get("", response_model=list[ProductListResponse])
def read_products(
    keyword: Annotated[str | None, Query(min_length=2)] = None,
    category: Annotated[str | None, Query(alias="p-category")] = None,
    limit: Annotated[int | None, Query(le=100)] = 20
):
    return product_service.read_products(keyword, category, limit)


# 상품 세부 정보
# 검증: product_id는 1 이상의 정수 (Path 검증)
@router.get("/{id}", response_model=ProductDetailResponse)
def read_product_by_id(
    id: Annotated[int, Path(ge=1, description="상품 고유 번호")]
):
    return product_service.read_product_by_id(id)


# 상품 수정
# 검증: product_id(Path) 및 ProductUpdate(Body) 검증
@router.put("/{id}", response_model=ProductDetailResponse)
def update_product(
    id: Annotated[int, Path(ge=1, description="상품 고유 번호")],
    data: ProductUpdate  # 선택적 필드만 수정 가능하도록
):
    return product_service.update_product(id, data)


# 상품 삭제
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    id: Annotated[int, Path(ge=1, description="상품 고유 번호")]
):
    product_service.delete_product(id)
