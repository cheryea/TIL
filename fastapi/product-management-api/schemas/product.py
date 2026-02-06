# product/schemas/product.py
from pydantic import BaseModel, Field, field_validator

# ---------------------------
#   상품 도메인 객체
# ---------------------------
class Product:
    def __init__(self, id, name, price, discount_price, stock, category):
        self.id = id
        self.name = name
        self.price = price
        self.discount_price = discount_price
        self.stock = stock
        self.category = category


# ---------------------------
#   공통 BaseModel (validator 재사용)
# ---------------------------
class ProductBase(BaseModel):
    name: str | None = None
    price: int | None = None
    discount_price: int | None = None
    stock: int | None = None
    category: str | None = None

    # discount_price가 price보다 크면 오류
    @field_validator("discount_price")
    def discount_must_be_less_than_price(cls, v, info):
        price = info.data.get("price")
        if v is not None and price is not None and v > price:
            raise ValueError("discount_price는 price보다 작아야 합니다.")
        return v


# ---------------------------
#   상품 등록 스키마 (필수값 + validation)
# ---------------------------
class ProductCreate(ProductBase):
    name: str = Field(..., min_length=2, max_length=50, alias="product_name", description="상품명")
    price: int = Field(..., ge=100, description="상품 가격 (100원 이상)")
    discount_price: int = Field(0, ge=0, description="할인 가격 (price보다 작아야 함)")
    stock: int = Field(10, ge=0, description="재고 (기본값 10)")
    category: str = Field(..., min_length=2, description="카테고리")


# ---------------------------
#   상품 수정 스키마 (선택적 필드)
# ---------------------------
class ProductUpdate(ProductBase):
    pass  # BaseModel에서 validator 재사용, 모든 필드 선택적


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
    final_price: int
    category: str
    stock: int
    is_sold_out: bool
