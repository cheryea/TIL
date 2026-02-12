# Post & Tag API 설계 문서 (N:M)

## 관계 요약

- Post : Tag = N : M

- 중간 테이블(association table)을 통해 Post와 Tag가 연결됨

- Post에는 comments 필드 존재 (상세 댓글 내용 포함), 단 댓글 API는 문서에서 생략

# 1. 태그(Tag) API
## 1-1. 태그 생성

### URL
```bash
POST /tags
```

### Request Body
```json
{
    "name": "점심"
}
```

#### 설명

- 새로운 태그 생성

태그 이름(name)은 유니크하게 관리

### Response Example
```json
{
    "id": 1,
    "name": "점심"
}
```
## 1-2. 태그 조회

### URL
```bash
GET /tags
```

### Response Example
```json
[
    { "id": 1, "name": "점심" },
    { "id": 2, "name": "일상" },
    { "id": 3, "name": "요리" }
]
```

#### 설명

- 모든 태그 리스트 반환

- 필요 시 Post 필터링 가능 (서비스 구현에 따라)

# 2. 게시글(Post) ↔ 태그(Tag) 연결 API
## 2-1. 게시글에 태그 추가

### URL
```bash
POST /posts/{post_id}/tags/{tag_name}
```

#### 설명

- 특정 게시글에 태그 연결

- post_id: URL 경로에서 받음

- tag_name: URL 경로에서 받음

- 이미 연결된 경우 중복 방지

## Response Example
```json
{
    "message": "Successfully added tag '점심' to post 1"
}
```
## 2-2. 게시글에서 태그 제거

### URL
```bash
DELETE /posts/{post_id}/tags/{tag_name}
```

#### 설명

- 특정 게시글에서 연결된 태그 제거

- Response: HTTP 204 No Content

## 2-3. 게시글 생성 시 태그 포함

### URL
```bash
POST /posts-db/with-tags
```

### Request Body Example
```json
{
    "title": "오늘 점심 메뉴",
    "content": "김치찌개 맛있었음",
    "tags": ["점심", "일상", "요리"]
}
```

### 설명

- 게시글 생성과 동시에 태그 연결 가능

- tags에 없는 태그는 서비스에서 자동 생성 가능

- 반환: PostDetailResponse 형태 (comments 필드 포함)

## Response Example
```json
{
    "id": 1,
    "title": "오늘 점심 메뉴",
    "content": "김치찌개 맛있었음",
    "comments": [
        {
            "id": 1,
            "content": "와 맛있겠다!"
        },
        {
            "id": 2,
            "content": "나도 오늘 점심 먹었음"
        }
    ],
    "tags": [
        { "id": 1, "name": "점심" },
        { "id": 2, "name": "일상" },
        { "id": 3, "name": "요리" }
    ]
}
```
# 3. PostDetailResponse 구조
| 필드       | 타입                    | 설명                                |
| -------- | --------------------- | --------------------------------- |
| id       | int                   | 게시글 ID                            |
| title    | str                   | 게시글 제목                            |
| content  | str                   | 게시글 내용                            |
| comments | list[CommentResponse] | 게시글에 달린 댓글 리스트 (단, 댓글 API는 문서 생략) |
| tags     | list[TagResponse]     | 게시글 태그 리스트                        |
