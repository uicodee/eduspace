from sqlalchemy import String, Integer, Text, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.models import BaseModel


class Course(BaseModel):

    __tablename__ = "course"

    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Float, default=0)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id", ondelete="CASCADE"))
