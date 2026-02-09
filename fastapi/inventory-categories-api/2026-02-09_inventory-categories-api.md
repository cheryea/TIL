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
