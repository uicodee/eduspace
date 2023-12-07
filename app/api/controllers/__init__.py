from fastapi import FastAPI
from .category import router as category_router
from .article import router as article_router


def setup(app: FastAPI) -> None:
    app.include_router(
        router=category_router,
        tags=["Category"]
    )
    app.include_router(
        router=article_router,
        tags=["Article"]
    )
