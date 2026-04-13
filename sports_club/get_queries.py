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

def get_member_and_recommender():
    return pd.read_sql("""
        SELECT DISTINCT m.firstname ||' '|| m.surname AS member,
        (
        SELECT r.firstname ||' '|| r.surname 
        FROM cd.members r
        WHERE m.recommendedby = r.memid
        ) AS recommender
        FROM cd.members m
        ORDER BY member
        """, engine)

def get_facilities_count():
    return pd.read_sql("""
        SELECT COUNT(*) AS "count"
        FROM cd.facilities
        """, engine)

def get_count_guestcost_10():
    return pd.read_sql("""
        SELECT COUNT(*) AS "count"
        FROM cd.facilities
        WHERE guestcost > 10
        """, engine)    

def get_count_recommendation_of_members():
    return pd.read_sql("""
        SELECT recommendedby, COUNT(memid) as "count"
        FROM cd.members
        WHERE recommendedby IS NOT NULL
        GROUP BY recommendedby
        ORDER BY recommendedby
        """, engine)

def get_total_slot_per_facility():
    return pd.read_sql("""
        SELECT facid, SUM(slots) AS "Total Slots"
        FROM cd.bookings
        GROUP BY facid
        ORDER BY facid
        """, engine)

def get_total_slots_booked_per_facility_per_month():
    return pd.read_sql("""
        SELECT facid, EXTRACT(MONTH FROM starttime) AS month, SUM(slots) AS "Total Slots"
        FROM cd.bookings
        WHERE starttime::date >= '2012-01-01' AND starttime::date < '2013-01-01'
        GROUP BY facid, month
        ORDER BY facid, month ASC
        """, engine)
        # can also use
        # where extract(year from starttime) = 2012

def get_revenue_per_facility():
    return pd.read_sql("""
        SELECT name,
        SUM(slots * CASE
                        WHEN memid = 0 THEN f.guestcost
                    ELSE
                        f.membercost
                    END) AS revenue
        FROM cd.facilities f
        INNER JOIN cd.bookings b
        ON b.facid = f.facid
        GROUP BY name
        ORDER BY revenue
        """, engine)

def get_total_revenue_less_than_1000():
    return pd.read_sql("""
        SELECT name,
        SUM(slots * CASE
                        WHEN memid = 0 THEN f.guestcost
                    ELSE
                        f.membercost
                    END) AS revenue
        FROM cd.facilities f
        INNER JOIN cd.bookings b
        ON b.facid = f.facid
        GROUP BY name
        HAVING SUM(slots * CASE
                        WHEN memid = 0 THEN f.guestcost
                    ELSE
                        f.membercost
                    END) < 1000
        ORDER BY revenue
        """, engine)

def get_highest_slots_booked():
    return pd.read_sql("""
        SELECT f.facid, SUM(slots) AS "Total Slots"
        FROM cd.bookings f
        GROUP BY f.facid
        ORDER BY SUM(slots) DESC
        LIMIT 1
        """, engine)

def get_total_slot_booked_per_facility_per_month():
    return pd.read_sql("""
        select facid, extract(month from starttime) as month, sum(slots) as slots
        from cd.bookings
            where
                starttime >= '2012-01-01'
                and starttime < '2013-01-01'
            group by rollup(facid, month)
        order by facid, month;   
        """, engine)

def get_total_hours_booked_per_facility():
    return pd.read_sql("""
        SELECT DISTINCT(f.facid), f.name, trim(to_char(sum(b.slots)/2.0, '999D99')) as "Total Hours"
        FROM cd.bookings b
        INNER JOIN cd.facilities f
        ON b.facid = f.facid
        GROUP BY f.facid , f.name
        ORDER BY f.facid 
        """, engine)

def get_each_member_first_booking_date():
    return pd.read_sql("""
        SELECT m.surname, m.firstname, m.memid, MIN(b.starttime) AS starttime 
        FROM cd.bookings b
        INNER JOIN cd.members m
        ON b.memid = m.memid
        WHERE starttime >= '2012-09-01'
        GROUP BY m.surname, m.firstname, m.memid
        ORDER BY memid
        """, engine)

def get_member_count_with_list_of_members():
    return pd.read_sql("""
        SELECT COUNT(*) OVER(), firstname, surname
        FROM cd.members
        ORDER BY joindate
        """, engine)
    # use window function to get total count of members while still listing each member's name

def get_numbered_list_of_members():
    return pd.read_sql("""
        SELECT row_number() OVER (ORDER BY joindate), firstname, surname
        FROM cd.members 
        """, engine)
    # use window function to get a numbered list of members ordered by their join date