from fastapi import APIRouter, status
from mysite3.services.post_service import post_service
from mysite3.schemas.post import PostCreate, PostDetailResponse, PostListResponse

router = APIRouter(prefix="/posts-mvc")


@router.post("", response_model=PostDetailResponse, status_code=status.HTTP_201_CREATED)
def create_post(data: PostCreate):
    return post_service.create_post(data)

# data: PostCreate
# - 클라이언트가 보낸 JSON 데이터를
# - Pydantic 모델인 PostCreate 객체로 변환하여 받음

# return post_service.create_post(data)
# - service 계층에서 비즈니스 로직을 처리하고
#   처리 결과를 반환함

# response_model=PostDetailResponse
# - 라우터는 반환된 결과를 PostDetailResponse 모델 형식으로 직렬화하여
#   JSON 형태로 클라이언트에게 응답함

# status_code=status.HTTP_201_CREATED
# - 요청이 성공적으로 처리되어 새로운 리소스가 생성되었음을
#   나타내는 HTTP 상태 코드 201(Created)을 클라이언트에게 반환


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

