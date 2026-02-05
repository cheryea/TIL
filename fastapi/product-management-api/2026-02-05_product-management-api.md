# 🛒 상품 관리 시스템 (Product Management System)

## 프로젝트 개요

FastAPI와 Pydantic 기반의 **상품 관리 API 프로젝트**입니다.

- 상품 등록, 조회, 수정, 삭제 (CRUD)
- 상품 목록 조회 및 검색 기능 (키워드/카테고리 필터링)
- `final_price`와 `is_sold_out` 계산 포함

---

## 1. 기능 소개

| 기능 | 설명 |
|------|------|
| 상품 등록 | 상품명, 가격, 할인, 재고, 카테고리 입력 후 등록 |
| 상품 상세 조회 | ID 기준 상품 단일 조회 |
| 상품 목록 조회 | 키워드/카테고리 필터링, limit 지정 가능 |
| 상품 수정 | 선택적 필드만 수정 가능 |
| 상품 삭제 | ID 기준 삭제 |
| 재고 상태 | `stock` 0이면 `is_sold_out` True |

---

## 2. 엔티티 / 데이터 구조

### 2.1 Product 엔티티

| 필드 | 타입 | 설명 |
|------|------|------|
| id | int | 상품 고유 식별자 |
| name | str | 상품명 |
| price | int | 원가 |
| discount_price | int | 할인 금액 |
| stock | int | 재고 수량 |
| category | str | 카테고리 |

### 2.2 Pydantic 스키마

#### 요청(Request)

**ProductCreate / ProductUpdate**

- name: 2~50자  
- price: 100 이상  
- discount_price: 0 이상, price보다 작아야 함  
- stock: 0 이상, 기본값 10  
- category: 2자 이상  

#### 응답(Response)

**ProductListResponse**

- id, name, final_price, category

**ProductDetailResponse**

- id, name, final_price, category, stock, is_sold_out  

> `final_price`와 `is_sold_out`은 Service에서 계산 후 Response 포함

---

## 3. API 엔드포인트

| Method | Path | 설명 | 요청 | 응답 |
|--------|------|------|------|------|
| POST | /products | 상품 등록 | ProductCreate | ProductDetailResponse |
| GET | /products | 상품 목록 조회 | Query: keyword, p-category, limit | list[ProductListResponse] |
| GET | /products/{id} | 상품 상세 조회 | Path: id | ProductDetailResponse |
| PUT | /products/{id} | 상품 수정 | ProductUpdate | ProductDetailResponse |
| DELETE | /products/{id} | 상품 삭제 | Path: id | HTTP 204 |

---

## 4. 예시 데이터

### 4.1 상품 등록

```json
{
  "product_name": "기계식 키보드",
  "price": 120000,
  "discount_price": 20000,
  "stock": 50,
  "category": "전자제품"
}
```
```json
{
  "product_name": "텀블러",
  "price": 25000,
  "discount_price": 2500,
  "stock": 100,
  "category": "생활용품"
}
```
```json
{
  "product_name": "티셔츠",
  "price": 39000,
  "discount_price": 0,
  "stock": 30,
  "category": "패션"
}
```
### 4.2 상품 상세 조회
```json
{
  "id": 1,
  "name": "기계식 키보드",
  "final_price": 100000,
  "category": "전자제품",
  "stock": 50,
  "is_sold_out": false
}
```
### 4.3 상품 목록 조회
```json
[
  {
    "id": 1,
    "name": "기계식 키보드",
    "final_price": 100000,
    "category": "전자제품"
  },
  {
    "id": 2,
    "name": "텀블러",
    "final_price": 22500,
    "category": "생활용품"
  }
]
```
## 5. 아키텍처 흐름
```
Client (Swagger / Postman)
          │
          ▼
      Router Layer
          │
          ▼
      Service Layer
  (final_price, is_sold_out 계산, 비즈니스 로직)
          │
          ▼
   Repository Layer
  (임시 DB CRUD)
          │
          ▼
       Product 객체
```
