from sqlalchemy import create_engine
from config import *

def get_engine():
    # Remove the commas and use standard assignment
    dbname = DB_NAME1
    user = DB_USER
    password = DB_PASSWORD
    host = DB_HOST
    port = DB_PORT

    url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
    return create_engine(url)
