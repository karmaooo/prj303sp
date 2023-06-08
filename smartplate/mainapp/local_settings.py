#########################################
##  IMPORT LOCAL SETTINGS ##
#########################################

try:
    from .local_settings import *
except ImportError:
    pass
import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("RAILWAY_POSTGRES_DB"),
        "USER": os.getenv("RAILWAY_POSTGRES_USER"),
        "PASSWORD": os.getenv("RAILWAY_POSTGRES_PASSWORD"),
        "HOST": os.getenv("RAILWAY_POSTGRES_HOST"),
        "PORT": os.getenv("RAILWAY_POSTGRES_PORT"),
    }
}
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "smartPlate",
#         "USER": "postgres",
#         "PASSWORD": "connect",
#         "HOST": "127.0.0.1",
#         "PORT": "5432",
#     } 
# }
