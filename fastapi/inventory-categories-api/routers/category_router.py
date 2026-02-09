from typing import Annotated
from fastapi import APIRouter, status, Path

from inventory.schemas.category import (
    CategoryCreate,
    CategoryDetailResponse,
    CategoryListResponse,
    CategoryUpdate,
)
from inventory.services.category_service import category_service

# -------------------
# Product Router
# -------------------
router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

# --------------------
# 카테고리 생성
# --------------------
@router.post(
    "",
    response_model=CategoryDetailResponse,
    status_code=status.HTTP_201_CREATED
)
def create_category(data: CategoryCreate):
    return category_service.create_category(data)


# --------------------
# 카테고리 전체 목록
# --------------------
@router.get(
    "",
    response_model=list[CategoryListResponse]
)
def read_categories():
    return category_service.read_categories()


# --------------------
# 카테고리 상세
# --------------------
@router.get(
    "/{category_id}",
    response_model=CategoryDetailResponse
)
def read_category_by_id(
    category_id: Annotated[int, Path(ge=1, description="카테고리 고유 번호")]
):
    return category_service.read_category_by_id(category_id)


# --------------------
# 카테고리 수정
# --------------------
@router.put(
    "/{category_id}",
    response_model=CategoryDetailResponse
)
def update_category(
    category_id: Annotated[int, Path(ge=1, description="카테고리 고유 번호")],
    data: CategoryUpdate
):
    return category_service.update_category(category_id, data)


# --------------------
# 카테고리 삭제
# --------------------
@router.delete(
    "/{category_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_category(
    category_id: Annotated[int, Path(ge=1, description="카테고리 고유 번호")]
):
    category_service.delete_category(category_id)

