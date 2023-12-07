from fastapi import APIRouter, Query

from app import dto
from app.api import schems

router = APIRouter(prefix="/category")


@router.get(path="/all")
async def get_categories() -> list[dto.Category]:
    ...


@router.get(path="/{category_id}")
async def get_category() -> dto.Category:
    ...


@router.post(path="/new")
async def new_category(
        category: schems.Category
) -> dto.Category:
    ...


@router.put(path="/edit")
async def edit_category(
        category: schems.EditCategory
) -> dto.Category:
    ...


@router.delete(path="/delete")
async def delete_category(category_id: int = Query(alias="categoryId")):
    ...

