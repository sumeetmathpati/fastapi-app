from starlette.middleware.authentication import AuthenticationMiddleware
from fastapi.routing import APIRoute
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

# Set all CORS enabled origins
# if settings.BACKEND_CORS_ORIGINS:
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=[
#           str(origin) for origin in settings.BACKEND_CORS_ORIGINS
#           ],
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )
