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

print("\nUnion of Products and TestProducts:")
print(union_products_and_testproducts())

print("\nUnion All of Products and TestProducts:")
print(union_all_products_and_testproducts())

print("\nInner Join of Customer Names with Orders:")
print(inner_join_customer_names_with_orders())

print("\nTotal Bill Per Customer:")
print(total_bill_per_customer())

print("\nBill Above $1000 Per Customer:")
print(bill_above_1000())