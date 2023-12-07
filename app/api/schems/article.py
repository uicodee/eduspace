from pydantic import BaseModel, Field


class Article(BaseModel):

    title: str
    text: str
    preview: str
    category_id: int = Field(alias="categoryId")


class EditArticle(Article):

    article_id: int = Field(alias="articleId")

