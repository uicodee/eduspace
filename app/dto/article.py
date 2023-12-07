from pydantic import Field

from app.dto import Base


class Article(Base):

    title: str
    views: int
    text: str
    preview: str
    category_id: int = Field(alias="categoryId")
