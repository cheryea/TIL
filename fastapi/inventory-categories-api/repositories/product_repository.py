from typing import List, Optional
from inventory.schemas.product import Product, ProductUpdate

class ProductRepository:
    def __init__(self):
        # 임시 메모리 DB
        self.products: List[Product] = []
        self._id_counter = 0  # PK 역할


    # -------------------------------
    # 상품 생성
    # -------------------------------
    def save(self, new_product: Product) -> Product:
        """
        새로운 상품 저장
        - new_product.id는 자동 부여
        """
        self._id_counter += 1
        new_product.id = self._id_counter
        self.products.append(new_product)
        return new_product


    # -------------------------------
    # 상품 전체 조회 (옵션 필터)
    # -------------------------------
    def list(
        self,
        keyword: Optional[str] = None,
        category_id: Optional[int] = None,
        limit: int = 20
    ) -> List[Product]:
        """
        상품 목록 조회
        - keyword: 상품명 검색 (선택)
        - category_id: 특정 카테고리 필터링 (선택)
        - limit: 최대 조회 수
        """
        result = self.products

        if keyword:
            result = [p for p in result if keyword.lower() in p.name.lower()]
        if category_id:
            result = [p for p in result if p.category_id == category_id]

        return result[:limit]


    # -------------------------------
    # ID로 상품 조회
    # -------------------------------
    def get_by_id(self, product_id: int) -> Optional[Product]:
        """
        상품 ID로 단일 조회
        """
        return next(
            (p for p in self.products if p.id == product_id),
            None
        )


    # -------------------------------
    # 상품 수정
    # -------------------------------
    def update(self, product: Product, data: ProductUpdate) -> Product:
        """
        상품 정보 수정
        - 선택 필드만 업데이트
        """
        for key, value in data.dict(exclude_unset=True).items():
            setattr(product, key, value)
        return product


    # -------------------------------
    # 상품 삭제
    # -------------------------------
    def delete(self, product_id: int) -> bool:
        """
        상품 삭제
        - 성공 시 True, 실패 시 False
        """
        for i, p in enumerate(self.products):
            if p.id == product_id:
                self.products.pop(i)
                return True
        return False
    
    
    # -------------------------------
    # 특정 카테고리에 상품 존재 여부
    # -------------------------------
    def exists_by_category_id(self, category_id: int) -> bool:
        """
        해당 카테고리에 속한 상품이 하나라도 있는지 확인
        """
        return any(p.category_id == category_id for p in self.products)


# Repository 싱글톤
product_repository = ProductRepository()
