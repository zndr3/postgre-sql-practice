import pandas as pd
from db import execute_change


def update_initialoutlay():
    sql = """
        UPDATE cd.facilities
        SET initialoutlay = 10000
        WHERE facid = 1
        """
    execute_change(sql)

def update_cost_for_tennis_court():
    sql = """
        UPDATE cd.facilities
        SET membercost = 6, guestcost = 30
        WHERE name LIKE 'Tennis Court%'
        """
    execute_change(sql)

def update_cost_by_10_percent():
    sql = """
        UPDATE cd.facilities f
        SET membercost = 
            (SELECT membercost * 1.1 FROM cd.facilities WHERE facid = 0),
            guestcost = 
            (SELECT guestcost * 1.1 FROM cd.facilities WHERE facid = 0)
        WHERE f.facid = 1
        """
    execute_change(sql)


