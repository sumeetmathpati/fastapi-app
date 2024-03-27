from starlette.middleware.authentication import AuthenticationMiddleware
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware

from app.create_app import create_app
from app.middleware.authentication import AuthMiddleware, authentication_error_handler
from app import di


def custom_generate_unique_id(route: APIRoute):
    return f"{route.tags[0]}-{route.name}"


app = create_app()

app.add_middleware(
    middleware_class=AuthenticationMiddleware,
    backend=AuthMiddleware(),
    on_error=authentication_error_handler
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
 ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
