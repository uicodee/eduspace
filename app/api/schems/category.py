from pydantic import BaseModel, Field


class Category(BaseModel):

    name: str


class EditCategory(Category):

    category_id: int = Field(alias="categoryId")
