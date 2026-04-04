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

# def get_who_used_tennis_court():
#     return pd.read_sql("""
#         SELECT DISTINCT m.firstname ||' '|| m.surname AS member, f.name AS facility
#         FROM cd.members m
#         INNER JOIN cd.bookings b 
#         ON b.memid = m.memid
#         INNER JOIN cd.facilities f
#         ON b.facid = f.facid
#         WHERE f.name LIKE 'Tennis Court%'
#         ORDER BY member
#         """, engine)

def get_member_facility_costs_on_date():
    return pd.read_sql("""
        SELECT m.firstname ||' '|| m.surname AS member, f.name AS facility,
        CASE
            WHEN m.memid = 0 THEN b.slots * f.guestcost
        ELSE
            b.slots * f.membercost
        END AS "cost"
        FROM cd.members m
        INNER JOIN cd.bookings b 
        ON b.memid = m.memid
        INNER JOIN cd.facilities f
        ON b.facid = f.facid
        WHERE b.starttime::date = '2012-09-14' AND 
        (CASE
            WHEN m.memid = 0 THEN b.slots * f.guestcost
        ELSE
            b.slots * f.membercost
        END) > 30
        ORDER BY cost DESC
        """, engine)