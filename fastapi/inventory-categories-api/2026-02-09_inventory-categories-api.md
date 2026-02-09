# inventory-categories-api 
(product-management-api 업그레이드 버전)

## 프로젝트 개요
기존 Product Management System을 업그레이드하여, 카테고리 기반 CRUD와 가격 검증 로직, 검색/조회 기능을 강화한 상품 관리 API 프로젝트입니다.

## 주요 기능
### 1. 카테고리 기반 CRUD
- 상품 등록, 조회, 수정, 삭제 기능을 **카테고리 단위로 관리**  
- RESTful URL 구조: `/categories/{category_id}/products/...`  
- 상품 단위뿐 아니라 카테고리 단위 관리가 가능하여 **데이터 구조와 접근성을 개선**

### 2. 가격 검증 로직
- 상품 가격과 할인 가격을 검증 (`discount_price <= price`)  
- 잘못된 가격 데이터 입력을 방지하여 **비즈니스 로직 안정성 확보**
- `final_price` 자동 계산: `price - discount_price`
- 재고가 0이면 품절 처리 (`is_sold_out=True`)

### 3. 상품 리스트 조회 및 검색
- 키워드 기반 검색 기능 지원 (최소 2자 입력)  
- 조회 개수 제한 설정 (`limit`, 기본 20, 최대 100)  
- 대규모 데이터에서도 **효율적인 리스트 조회** 가능

### 4. 서비스-레포지토리 계층 구조
- **Repository**: DB 접근 및 CRUD 처리 담당  
- **Service**: 비즈니스 로직 처리  
- 계층 분리를 통해 **코드 유지보수성 향상** 및 테스트 용이성 확보

### 5. FastAPI와 Pydantic 적용
- **FastAPI**: 빠르고 효율적인 API 서버 구축  
- **Pydantic**: 데이터 검증 및 타입 안전성 제공  
- 안정적이고 직관적인 API 문서(Swagger) 자동 생성

### 6. 기타
- 싱글톤 패턴 활용 → 임시 DB에서 카테고리/상품별 단일 객체 사용
- 카테고리 삭제 시 해당 카테고리에 상품이 존재하면 삭제 불가 오류 처리
- 카테고리 조회 시, `category_id` 검증 후 이름 및 상품 정보 응답

## 3. API 엔드포인트

### 카테고리
| Method | Path | 설명 | 요청/파라미터 | 응답 |
|--------|------|------|----------------|------|
| POST   | /categories | 카테고리 등록 | Body: CategoryCreate | CategoryDetailResponse |
| GET    | /categories | 카테고리 전체 목록 조회 | - | list[CategoryListResponse] |
| GET    | /categories/{id} | 단일 카테고리 조회 | Path: id | CategoryDetailResponse |
| PUT    | /categories/{id} | 카테고리 이름 수정 | Body: CategoryUpdate, Path: id | CategoryDetailResponse |
| DELETE | /categories/{id} | 카테고리 삭제 (상품 존재 시 오류) | Path: id | HTTP 204 |

예시: CategoryCreate
```json
{
  "name": "전자제품"
}
```
예시: CategoryDetailResponse

```json
{
  "id": 1,
  "name": "전자제품"
}
```
### 상품 (카테고리 하위 리소스)
| Method | Path | 설명 | 요청/파라미터 | 응답 |
|--------|------|------|----------------|------|
| POST   | /categories/{category_id}/products | 카테고리 내 상품 등록 | Body: ProductCreate, Path: category_id | ProductDetailResponse |
| GET    | /categories/{category_id}/products | 카테고리 내 상품 목록 조회 | Path: category_id, Query: keyword, limit (default=20, max=100) | list[ProductListResponse] |
| GET    | /categories/{category_id}/products/{id} | 단일 상품 상세 조회 | Path: category_id, id | ProductDetailResponse |
| PUT    | /categories/{category_id}/products/{id} | 단일 상품 수정 | Body: ProductUpdate, Path: category_id, id | ProductDetailResponse |
| DELETE | /categories/{category_id}/products/{id} | 단일 상품 삭제 | Path: category_id, id | HTTP 204 |

예시: ProductCreate
```json
{
  "name": "기계식 키보드",
  "price": 120000,
  "discount_price": 20000,
  "stock": 50
}
```

예시: ProductDetailResponse
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

예시: ProductListResponse
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

## 현재 프로젝트 구조 (예시)
```
inventory/
├─ repositories/        # DB 접근 계층 (CRUD 담당)
│  ├─ category_repository.py
│  └─ product_repository.py
├─ services/            # 비즈니스 로직 계층
│  ├─ category_service.py
│  └─ product_service.py
├─ routers/             # API 라우터 (FastAPI 엔드포인트)
│  ├─ category_router.py
│  └─ product_router.py
└─ schemas/             # Pydantic 모델 (데이터 검증 및 직렬화)
   ├─ category.py
   └─ product.py
```

### 구조 설명
#### 1. routers
- FastAPI 라우터
- 각 엔드포인트에서 서비스 호출
- 카테고리 기준 URL 구조 /categories/{category_id}/products/...
- Swagger 문서 자동 생성
#### 2. schemas
- Pydantic 모델 정의
- Request/Response 데이터 검증 및 직렬화
- ProductCreate, ProductUpdate, ProductDetailResponse 등
#### 3. services
- 비즈니스 로직 처리
- Repository를 사용하여 데이터 조작 후 결과 반환
- 가격 검증, 재고 상태 계산 등 추가 로직 포함
#### 4. repositories
- DB 접근 전담
- category_repository, product_repository
- CRUD 기본 기능 구현
- 모듈 레벨에서 객체를 생성 → 싱글톤처럼 사용 가능
#### 5. schemas
- Pydantic 모델 정의
- Request/Response 데이터 검증 및 직렬화
- ProductCreate, ProductUpdate, ProductDetailResponse 등
