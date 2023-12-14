from pydantic import parse_obj_as
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app import dto
from app.api import schems
from app.infrastructure.database.dao.rdb import BaseDAO
from app.infrastructure.database.models import Category, Article


class CategoryDAO(BaseDAO[Category]):
    def __init__(self, session: AsyncSession):
        super().__init__(Category, session)

    async def add_category(self, category: schems.Category) -> dto.Category:
        result = await self.session.execute(
            insert(Article).values(
                name=category.name
            ).returning(
                Category
            )
        )
        await self.session.commit()
        return dto.Category.from_orm(result.scalar())

    async def get_category(self, category_id: int) -> dto.Category:
        result = await self.session.execute(
            select(Category).where(Category.id == category_id)
        )
        category = result.scalar()
        if category is not None:
            return dto.Category.from_orm(category)

    async def get_categories(self) -> list[dto.Category]:
        result = await self.session.execute(
            select(Category)
        )
        return parse_obj_as(list[dto.Category], result.scalars().all())

    async def edit_category(self, category: schems.EditCategory) -> dto.Category:
        result = await self.session.execute(
            update(Category).values(
                name=category.name
            ).where(Category.id == category.category_id).returning(
                Category
            )
        )
        await self.session.commit()
        return dto.Category.from_orm(result.scalar())

    async def delete_category(self, category_id: int) -> None:
        await self.session.execute(
            delete(Category).where(Category.id == category_id)
        )
        await self.session.commit()
