from typing import List, Optional
from inventory.schemas.category import Category, CategoryUpdate


class CategoryRepository:
    def __init__(self):
        # 임시 DB
        self.categories: List[Category] = []
        self._id_counter = 0


    # -------------------------------
    # 카테고리 생성
    # -------------------------------
    def save(self, new_category: Category) -> Category:
        # <-- db를 사용하면 없어질 로직
        self._id_counter += 1
        new_category.category_id = self._id_counter
        # -->
        self.categories.append(new_category)
        return new_category


    # -------------------------------
    # 전체 카테고리 조회
    # -------------------------------
    def list(self) -> List[Category]:
        return self.categories


    # -------------------------------
    # ID로 카테고리 조회
    # -------------------------------
    def get_by_id(self, category_id: int) -> Optional[Category]:
        return next(
            (c for c in self.categories if c.category_id == category_id),
            None
        )


    # -------------------------------
    # 이름으로 카테고리 조회
    # -------------------------------
    def get_by_name(self, name: str) -> Optional[Category]:
        return next(
            (c for c in self.categories if c.name.lower() == name.lower()),
            None
        )


    # -------------------------------
    # 카테고리 수정
    # -------------------------------
    def update(self, category: Category, data: CategoryUpdate) -> Category:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(category, key, value)
        return category


    # -------------------------------
    # 카테고리 삭제
    # -------------------------------
    def delete(self, category_id: int) -> bool:
        for i, c in enumerate(self.categories):
            if c.category_id == category_id:
                self.categories.pop(i)
                return True
        return False

# Repository 싱글톤
category_repository = CategoryRepository()
