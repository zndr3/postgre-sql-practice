from get_queries import *
from insert_queries import *

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

def insert_queries():
    insert_new_facility()
    print("Facilities:")
    print(get_facilities())

    insert_2_new_facilities()
    print("\nFacilities:")
    print(get_facilities())


if __name__ == "__main__":
    # get_queries()
    insert_queries()