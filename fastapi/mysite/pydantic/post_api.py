# post_api.py
from fastapi import APIRouter
from .post import PostCreate, Post

# 경로 접두사 설정
router = APIRouter(prefix="/posts-pydantic")

# 게시글 저장소 역할을 수행하는 리스트
posts = []
# 고유 식별자 생성을 위한 카운터
post_id = 0


@router.post("")
def create_post(post_data: PostCreate):
    # post_data에는 제목, 내용이라는 필드만 들어가야 합니다.
    # basemodel을 통해 제목, 내용만 들어있도록 강제한다.
    global post_id
    post_id += 1

    post = Post(post_id, post_data.title, post_data.content)

    posts.append(post)

    return post


@router.get("")
def read_posts():
    # 저장된 모든 게시글 반환
    return posts

@router.get("/{id}")
def read_post(id: int):
    # 식별자가 일치하는 데이터를 리스트에서 탐색
    for post in posts:
        if post.id == id:
            return post
    return {"message": "데이터를 찾을 수 없습니다."}

@router.put("/{id}")
def update_post(id: int, updated_post: PostCreate):
    for post in posts:
        if post.id == id:
            # 전달받은 객체의 필드값으로 기존 데이터 갱신
            post.title = updated_post.title
            post.content = updated_post.content
            return post
    return {"message": "수정할 대상이 없습니다."}

@router.delete("/{id}")
def delete_post(id: int):
    for index, post in enumerate(posts):
        if post.id == id:
            # 해당 인덱스의 요소를 추출하여 제거
            return posts.pop(index)
    return {"message": "삭제할 대상이 없습니다."}
