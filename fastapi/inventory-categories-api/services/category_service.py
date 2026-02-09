from typing import List
from fastapi import HTTPException

from inventory.schemas.category import (
    Category,
    CategoryCreate,
    CategoryUpdate,
    CategoryListResponse,
    CategoryDetailResponse,
)
from inventory.repositories import category_repository
from inventory.repositories import product_repository


class CategoryService:

    # 카테고리 검증 메서드
    def _get_category_or_404(self, category_id: int) -> Category:
        category = category_repository.get_by_id(category_id)
        if not category:
            raise HTTPException(status_code=404, detail="카테고리를 찾을 수 없습니다.")
        return category


    # --------------------
    # 카테고리 생성
    # --------------------
    def create_category(self, data: CategoryCreate) -> CategoryDetailResponse:
        category = Category(
            category_id=None,
            name=data.name,
        )
        saved = category_repository.save(category)
        return self._to_detail_response(saved)


    # --------------------
    # 카테고리 전체 목록
    # --------------------
    def read_categories(self) -> List[CategoryListResponse]:
        categories = category_repository.list()
        return [self._to_list_response(c) for c in categories]


    # --------------------
    # 카테고리 상세
    # --------------------
    def read_category_by_id(self, category_id: int) -> CategoryDetailResponse:
        category = self._get_category_or_404(category_id)
        return self._to_detail_response(category)


    # --------------------
    # 카테고리 수정
    # --------------------
    def update_category(
        self, category_id: int, data: CategoryUpdate
    ) -> CategoryDetailResponse:
        category = self._get_category_or_404(category_id)

        updated = category_repository.update(category, data)
        return self._to_detail_response(updated)


    # --------------------
    # 카테고리 삭제
    # --------------------
    def delete_category(self, category_id: int) -> None:
        # 해당 카테고리에 상품이 있는지 확인
        if product_repository.exists_by_category_id(category_id):
            raise HTTPException(
                status_code=400,
                detail="해당 카테고리에 상품이 존재하여 삭제할 수 없습니다."
            )

        if not category_repository.delete(category_id):
            raise HTTPException(status_code=404, detail="카테고리를 찾을 수 없습니다.")


    # --------------------
    # 응답 매핑
    # --------------------
    def _to_list_response(self, category: Category) -> CategoryListResponse:
        return CategoryListResponse(
            id=category.id,
            name=category.name,
        )

    def _to_detail_response(self, category: Category) -> CategoryDetailResponse:
        return CategoryDetailResponse(
            id=category.id,
            name=category.name,
        )


# 싱글톤
category_service = CategoryService()
