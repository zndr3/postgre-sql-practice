import pandas as pd
from db import get_engine

# Create the engine once at the top to reuse it
engine = get_engine()

def get_facilities():
    return pd.read_sql("""
        SELECT * FROM cd.facilities
        """, engine)

def get_facilities_and_membercost():
    return pd.read_sql("""
        SELECT name, membercost
        FROM cd.facilities
        """, engine)

def get_facilities_that_charges():
    return pd.read_sql("""
        SELECT name, membercost
        FROM cd.facilities
        WHERE membercost > 0
        """, engine)