from get_queries import *
from insert_queries import *
from update_queries import *

def get_queries():
    print("Facilities:")
    print(get_facilities())

    print("\nFacilities and Member Cost:")
    print(get_facilities_and_membercost())

    print("\nFacilities that Charge:")
    print(get_facilities_that_charges())

    print("\nCheap and Expensive Facilities:")
    print(get_cheap_and_expensive_facilities())

    print("\nLatest Joined Date:")
    print(get_latest_joined_date())

    print("\nPeople That Recommended:")
    print(get_people_that_recommended())

    print("\nMember and Recommended By:")
    print(get_member_and_recommended_by())

    print("\nMember, Facility, and Cost on Date:")
    print(get_member_facility_costs_on_date())

    print("\nMember and Recommender:")
    print(get_member_and_recommender())

    print("\nFacilities Count:")
    print(get_facilities_count())

    print("\nFacilities with Costly Maintenance:")
    print(get_count_guestcost_10())

    print("\nMembers Who Recommended Others:")
    print(get_count_recommendation_of_members())

    print("\nTotal Slot per Facility:")
    print(get_total_slot_per_facility())

    print("\nTotal Slots Booked per Facility per Month:")
    print(get_total_slots_booked_per_facility_per_month())

    print("\nTotal Revenue per Facility:")
    print(get_revenue_per_facility())

    print("\nTotal Revenue per Facility less than 1000:")
    print(get_total_revenue_less_than_1000())

    print("\nHighest Slot Booked Facility:")
    print(get_highest_slots_booked())

    print("\nTotal Slots Booked per Facility per Month:")
    print(get_total_slot_booked_per_facility_per_month())

    print("\nTotal Hours Booked per Facility per Month:")
    print(get_total_hours_booked_per_facility())

    print("\nEach Member's First Booking Date:")
    print(get_each_member_first_booking_date())

    print("\nTotal Member Count and List of Member Names:")
    print(get_member_count_with_list_of_members())

    print("\nNumbered List of Members:")
    print(get_numbered_list_of_members())

def insert_queries():
    insert_new_facility()
    print("Facilities:")
    print(get_facilities())

    insert_2_new_facilities()
    print("\nFacilities:")
    print(get_facilities())

def update_queries():
    update_initialoutlay()
    print("Facilities:")
    print(get_facilities())

if __name__ == "__main__":
    get_queries()
    # insert_queries()
    # update_queries()