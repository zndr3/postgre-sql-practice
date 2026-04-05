from sqlalchemy import create_engine, text
from config import *

def get_engine():
    # Remove the commas and use standard assignment
    dbname = DB_NAME2
    user = DB_USER
    password = DB_PASSWORD
    host = DB_HOST
    port = DB_PORT

    url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
    return create_engine(url)

# Create a global engine instance to reuse
engine = get_engine()

def execute_change(sql_string):
    """Handles INSERT, UPDATE, and DELETE with automatic commit."""
    with engine.connect() as conn:
        conn.execute(text(sql_string))
        conn.commit()