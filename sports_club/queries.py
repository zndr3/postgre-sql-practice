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

def get_cheap_and_expensive_facilities():
    return pd.read_sql("""
        SELECT name, 
        CASE WHEN monthlymaintenance > 100 THEN 'expensive'
        ELSE 'cheap'
        END AS cost
        FROM cd.facilities;
        """, engine)

def get_latest_joined_date():
    return pd.read_sql("""
        SELECT firstname, surname, joindate
        FROM cd.members
        WHERE joindate = (SELECT MAX(joindate) FROM cd.members)
        """, engine)

def get_people_that_recommended():
    return pd.read_sql("""
        SELECT DISTINCT(m2.firstname), m2.surname
        FROM cd.members m1
        INNER JOIN cd.members m2
        ON m1.recommendedby = m2.memid
        ORDER BY m2.surname;
        """, engine)

def get_member_and_recommended_by():
    return pd.read_sql("""
        SELECT member.firstname AS memfname, member.surname AS memsname, 
	    reco.firstname AS recfname, reco.surname AS recsname
        FROM cd.members member
        LEFT JOIN cd.members reco
        ON member.recommendedby = reco.memid
        ORDER BY member.surname, member.firstname
        """, engine)