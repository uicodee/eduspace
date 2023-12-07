from sqlalchemy import String, Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.models import BaseModel


class Video(BaseModel):

    __tablename__ = "video"

    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(Text)
    views: Mapped[int] = mapped_column(Integer, default=0)
    preview: Mapped[str] = mapped_column(String)
    course_id: Mapped[int] = mapped_column(ForeignKey("course.id", ondelete="CASCADE"))
