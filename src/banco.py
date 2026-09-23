from urllib.parse import quote_plus
from sqlalchemy import create_engine
from config import *

def conectar():

    senha = quote_plus(DB_PASSWORD)

    connection_string = (
        f"mysql+pymysql://"
        f"{DB_USER}:{senha}"
        f"@{DB_HOST}:{DB_PORT}"
        f"/{DB_NAME}"
    )

    return create_engine(connection_string)