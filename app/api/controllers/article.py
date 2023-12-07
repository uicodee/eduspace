from fastapi import APIRouter, Query

from app import dto
from app.api import schems

router = APIRouter(prefix="/article")


@router.get(path="/all")
async def get_articles() -> list[dto.Article]:
    ...


@router.get(path="/{article_id}")
async def get_article() -> dto.Article:
    ...


@router.post(path="/new")
async def new_article(
        article: schems.Article
) -> dto.Article:
    ...


@router.put(path="/edit")
async def edit_article(
        article: schems.EditArticle
) -> dto.Article:
    ...


@router.delete(path="/delete")
async def delete_article(
        article_id: int = Query(alias="articleId")
):
    ...

