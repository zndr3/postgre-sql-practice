import pandas as pd
from db import execute_change


def delete_all_bookings():
    sql = """
        DELETE FROM cd.bookings
        """
    execute_change(sql)

def truncate_bookings_table():
    sql = """
        TRUNCATE TABLE cd.bookings
        """
    execute_change(sql)

def delete_member_id():
    sql = """
        DELETE FROM cd.members
        WHERE memid = 37
        """
    execute_change(sql)

def delete_member_not_in_bookings():
    sql = """
        DELETE
        FROM cd.members m
        WHERE m.memid NOT IN (
            SELECT b.memid
            FROM cd.bookings b)
        """
    execute_change(sql)

