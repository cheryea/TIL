# services/post_service.py

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from mysite4.repositories.post_repository import post_repository
from mysite4.models.post import Post
from mysite4.schemas.post import PostCreate


class PostService:
    def create_post(self, db: Session, data: PostCreate):
        new_post = Post(title=data.title, content=data.content)

        # 레포지토리에 저장을 요청한다. (아직 DB에 확정된 상태는 아님)
        post_repository.save(db, new_post)

        # 서비스 계층에서 트랜잭션을 최종 확정한다.
        db.commit()

        # DB에서 생성된 ID 등을 파이썬 객체에 반영한다.
        db.refresh(new_post)

        return new_post

    def read_posts(self, db: Session):
        return post_repository.find_all(db)

    def read_post_by_id(self, db: Session, id: int):
        post = post_repository.find_by_id(db, id)
        (db, id)
        if not post:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND, "존재하지 않는 게시글입니다."
            )
        return post

    def update_post(self, db: Session, id: int, data: PostCreate):
        # 수정할 게시글 존재 여부를 먼저 확인한다.
        post = self.read_post_by_id(db, id)

        # 레포지토리를 통해 객체 정보를 수정(더티 체크 대상)한다.
        updated_post = post_repository.update(db, post, data)

        # 최종 확정 및 갱신
        db.commit()
        db.refresh(updated_post)

        return updated_post

    def delete_post(self, db: Session, id: int):
        post = self.read_post_by_id(db, id)

        post_repository.delete(db, post)

        # 삭제 트랜잭션을 확정한다.
        db.commit()


post_service = PostService()
