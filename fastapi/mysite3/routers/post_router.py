from fastapi import APIRouter, status
from mysite3.services.post_service import post_service
from mysite3.schemas.post import PostCreate, PostDetailResponse, PostListResponse

router = APIRouter(prefix="/posts-mvc")


@router.post("", response_model=PostDetailResponse, status_code=status.HTTP_201_CREATED)
def create_post(data: PostCreate):
    return post_service.create_post(data)

# data: PostCreate
# - 클라이언트가 보낸 JSON 요청 데이터를
# - PostCreate 객체로 변환해서 받음

# return post_service.create_post(data)
# - service에서 비즈니스 로직을 처리한 결과를 반환

# response_model=PostDetailResponse
# - router는 그 결과를 PostDetailResponse 형식으로 직렬화해서
#   클라이언트(JSON)에게 응답함



@router.get("", response_model=list[PostListResponse])
def read_posts():
    return post_service.read_posts()


@router.get("/{id}", response_model=PostDetailResponse)
def read_post_by_id(id: int):
    return post_service.read_post_by_id(id)


@router.put("/{id}", response_model=PostDetailResponse)
def update_post(id: int, data: PostCreate):
    return post_service.update_post(id, data)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    post_service.delete_post(id)

