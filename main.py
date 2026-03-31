from queries import *

print("Products with Categories:")
print(show_products_with_categories())

print("\nCustomers:")
print(show_customers())

print("\nProducts with Categories (Left Join):")
print(left_join_products_and_categories())

print("\nProducts with Categories (Right Join):")
print(right_join_products_and_categories())

print("\nProducts with Categories (Full Join):")
print(full_join_products_and_categories())

print("\nProducts with Categories (Cross Join):")
print(cross_join_products_and_categories())