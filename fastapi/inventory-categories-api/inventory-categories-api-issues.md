## 1. 검증 로직 개선

### 문제

기존 코드는 상품과 카테고리 검증, 조회, 일치 확인을 한 메서드에서 모두 처리:

```python
def _validate_product_and_category(self, product_id: int | None = None, category_id: int | None = None):
    category = None
    product = None

    if category_id is not None:
        category = category_repository.get_by_id(category_id)
        if not category:
            raise HTTPException(status_code=404, detail="해당 카테고리가 존재하지 않습니다.")

    if product_id is not None:
        product = product_repository.get_by_id(product_id)
        if not product or (category_id is not None and product.category_id != category_id):
            raise HTTPException(status_code=404, detail="해당 카테고리의 상품을 찾을 수 없습니다.")

    return product, category
```
### 문제점
- 튜플 반환 → 호출부에서 언패킹 필요

- 상품 부재 / 카테고리 불일치 시 메시지가 동일 → 문제 원인 불분명

- 단일 책임 위반 가능 (상품 조회 + 카테고리 존재 확인 + 일치 검증 혼재)

### 해결
검증을 목적별 메서드로 분리:

```python
def _get_category_or_404(self, category_id: int):
    category = category_repository.get_by_id(category_id)
    if not category:
        raise HTTPException(404, "해당 카테고리가 존재하지 않습니다.")

def _get_product_or_404(self, product_id: int, category_id: int | None = None):
    product = product_repository.get_by_id(product_id)
    if not product:
        raise HTTPException(404, "상품을 찾을 수 없습니다.")
    if category_id is not None and product.category_id != category_id:
        raise HTTPException(404, "해당 카테고리의 상품이 아닙니다.")
    return product
```
### 장점
- 단일 책임 준수

- 상품 부재 / 카테고리 불일치 등 경우를 명확하게 구분

- 호출부에서 튜플 언패킹 불필요

- 서비스 레이어에서 잘못된 데이터 접근 방지

## 2. 네이밍 및 JSON 응답 개선
### 문제
```python
# 상품
name: str = Field(..., alias="product_name", description="상품명")

# 카테고리
name: str = Field(..., description="카테고리")
```
- 상품은 alias 적용, 카테고리는 원본 name → JSON 응답 불일치

- 내부 모델과 API 응답이 달라 클라이언트 혼동 가능

- 도메인 필드명이 동일 → 리스트 API 등에서 혼동 발생

### 해결
```python
# 상품
name: str = Field(..., description="상품명")

# 카테고리
category_name: str = Field(..., description="카테고리명")
```
### 장점
- 상품: name, 카테고리: category_name으로 도메인 명확

- JSON 응답과 내부 모델 일치 → 클라이언트 혼동 최소화

- 리스트 API에서 여러 도메인 값이 섞여도 즉시 구분 가능

- Swagger/OpenAPI 문서와 실제 응답 일치 → alias 확인 불필요

- 유지보수 시 혼동 감소, 다른 도메인 추가에도 안전

#### 예시
```json
{
  "id": 1,
  "name": "아이폰",
  "category_name": "전자기기"
}
```
직관적이고 명시적
