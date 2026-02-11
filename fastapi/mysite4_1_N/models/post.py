from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text
from database import Base
from typing import TYPE_CHECKING

# 타입 힌트용
if TYPE_CHECKING:
    from .comment import Comment


class Post(Base):
    __tablename__ = "posts"

    # primary_key=True → 기본키
    # autoincrement=True → 자동 증가
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    # nullable=False → 필수 입력
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)

    # type 힌트: list["Comment"]
    # relationship(관계 정의)

    # "Comment" → 연결된 모델 클래스
    # back_populates="post" → Comment 모델에서 post 필드와 연결
    # "all" = 모든 행동을 자식에게 전파, "delete-orphan" = 부모(Post)와 연결이 끊긴 자식(Comment)은 DB에서 삭제
    # 예) 게시글 삭제 시 관련 댓글도 자동 삭제
    comments: Mapped[list["Comment"]] = relationship(
        "Comment", back_populates="post", cascade="all, delete-orphan"
    )
