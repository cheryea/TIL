# mysite4/models/__init__.py

from .post import Post
from .comment import Comment
from database import Base

__all__ = ["Base", "Post", "Comment"]
