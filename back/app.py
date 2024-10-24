from fastapi import FastAPI
from back.settings import settings


def create_app():
    app = FastAPI(
        debug=settings.debug,
        docs_url='/api/docs',
        title='FARM Example',
    )

    return app

