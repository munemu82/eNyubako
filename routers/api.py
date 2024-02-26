from fastapi import APIRouter

# from ..config import ROUTE_PREFIX_V1
API_PREFIX = "/api"

JWT_TOKEN_PREFIX = "Authorization"

ROUTE_PREFIX_V1 = "/v1"

from . import userRoute

router = APIRouter()

def include_api_routes():
    ''' Include to router all api rest routes with version prefix '''
  #  router.include_router(auth.router)
    router.include_router(userRoute.router, prefix=ROUTE_PREFIX_V1)

include_api_routes()