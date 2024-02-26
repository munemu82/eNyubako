from typing import List

# from starlette.config import Config

# from starlette.datastructures import CommaSeparatedStrings, Secret


###
# Properties configurations
###

API_PREFIX = "/api"

JWT_TOKEN_PREFIX = "Authorization"

# config = Config("C:/Users/amosm/OneDrive/Documents/ProgrammingProjects/Python - 2024/FASTAPI Projects/fastapi-bigger-application-master/app/src/.env")

ROUTE_PREFIX_V1 = "/v1"


ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
SECRET_KEY = "amossecretm@$@&^@&%^&RFghgjvbdsha" 
JWT_REFRESH_SECRET_KEY = "amos13ugfdfgh@#$%^@&jkl45678902"


""" ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
) """
