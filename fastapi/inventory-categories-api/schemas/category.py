# product/schemas/product.py
from pydantic import BaseModel, Field

# ---------------------------
#   카테고리 도메인 객체
# ---------------------------
class Category:
    def __init__(self, category_name: str, category_id: int | None = None):
        self.category_id = category_id
        self.category_name = category_name


# ---------------------------
#   카테고리 생성 스키마
# ---------------------------
class CategoryCreate(BaseModel):
    category_name: str = Field(..., min_length=2, max_length=50, description="카테고리")


# ---------------------------
#   상품 수정 스키마 (선택적 필드)
# ---------------------------
class CategoryUpdate(BaseModel):
    category_name: str | None = Field(None, min_length=2, max_length=50, description="카테고리 이름")


# ---------------------------
#   상품 조회 응답 스키마
# ---------------------------
class CategoryListResponse(BaseModel):
    category_id: int
    category_name: str


class CategoryDetailResponse(BaseModel):
    category_id: int
    category_name: str
