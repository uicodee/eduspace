from fastapi import APIRouter, Query, Path, Depends

from app import dto
from app.api import schems
from app.api.dependencies import dao_provider
from app.infrastructure.database.dao import HolderDao

router = APIRouter(prefix="/category")


@router.get(path="/all")
async def get_categories(
        dao: HolderDao = Depends(dao_provider)
) -> list[dto.Category]:
    return await dao.category.get_categories()


@router.get(path="/{category_id}")
async def get_category(
        category_id: int = Path(),
        dao: HolderDao = Depends(dao_provider)
) -> dto.Category:
    return await dao.category.get_category(category_id=category_id)


@router.post(path="/new")
async def new_category(
        category: schems.Category,
        dao: HolderDao = Depends(dao_provider)
) -> dto.Category:
    return await dao.category.add_category(category=category)


@router.put(path="/edit")
async def edit_category(
        category: schems.EditCategory,
        dao: HolderDao = Depends(dao_provider)
) -> dto.Category:
    return await dao.category.edit_category(category=category)


@router.delete(path="/delete")
async def delete_category(
        category_id: int = Query(alias="categoryId"),
        dao: HolderDao = Depends(dao_provider)
):
    return await dao.category.delete_category(category_id=category_id)

