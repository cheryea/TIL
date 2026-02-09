# product/schemas/product.py
from pydantic import BaseModel, Field

# ---------------------------
#   상품 도메인 객체
# ---------------------------
class Product:
    def __init__(self, id, category_id, name, price, discount_price, stock):
        self.id = id
        self.category_id = category_id
        self.name = name
        self.price = price
        self.discount_price = discount_price
        self.stock = stock


# ---------------------------
#   상품 등록 스키마 (필수값 + validation)
# ---------------------------
class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="상품명")
    price: int = Field(..., ge=100, description="상품 가격 (100원 이상)")
    discount_price: int = Field(0, ge=0, description="할인 가격 (price보다 작아야 함)")
    stock: int = Field(10, ge=0, description="재고 (기본값 10)")


# ---------------------------
#   상품 수정 스키마 (선택적 필드)
# ---------------------------
class ProductUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=50, description="상품명")
    price: int | None = Field(None, ge=100, description="상품 가격 (100원 이상)")
    discount_price: int | None = Field(None, ge=0, description="할인 가격 (price보다 작아야 함)")
    stock: int | None = Field(None, ge=0, description="재고 (기본값 10)")


# ---------------------------
#   상품 조회 응답 스키마
# ---------------------------
class ProductListResponse(BaseModel):
    id: int
    name: str
    final_price: int
    category: str


class ProductDetailResponse(BaseModel):
    id: int
    name: str
    price: int
    discount_price: int
    final_price: int
    category: str
    stock: int
    is_sold_out: bool
