from pydantic import Field

from app.dto import Base


class Course(Base):

    title: str
    description: str
    category_id: int = Field(alias="categoryId")
    price: float
