from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class SocialMediaPost(Base):

    __tablename__ = "social_media_posts"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    post_id: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    platform: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    user_id: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    caption: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    likes: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    comments: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    shares: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    reach: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    timestamp: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )