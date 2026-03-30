from queries import show_products_with_categories, show_customers

print("Products with Categories:")
for row in show_products_with_categories():
    print(row)

print("\nCustomers:")
for row in show_customers():
    print(row)