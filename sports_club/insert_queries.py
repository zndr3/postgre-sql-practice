import pandas as pd
from db import execute_change


def insert_new_facility():
    sql = """
        INSERT INTO cd.facilities (facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)
        VALUES (9, 'Spa', 20, 30, 100000, 800)
        ON CONFLICT (facid) DO NOTHING
        """
    execute_change(sql)

def insert_2_new_facilities():
    sql = """
        INSERT INTO cd.facilities (facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)
        VALUES (9, 'Spa', 20, 30, 100000, 800), (10, 'Squash Court 2', 3.5, 17.5, 5000, 80)
        ON CONFLICT (facid) DO NOTHING
        """
    execute_change(sql)
