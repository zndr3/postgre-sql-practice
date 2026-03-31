import pandas as pd
from db import get_engine

# Create the engine once at the top to reuse it
engine = get_engine()

def show_products_with_categories():
    return pd.read_sql("""
        SELECT p.product_name, c.category_name
        FROM products p
        INNER JOIN categories c
        ON p.category_id = c.category_id
        """, engine)

def show_customers():
    # Update this query to pull from your customers table
    return pd.read_sql("""
        SELECT customer_name, contact_name, city 
        FROM customers
        """, engine)


def left_join_products_and_categories():
    return pd.read_sql("""
        SELECT tp.testproduct_id, tp.product_name, c.category_name
        FROM testproducts tp
        LEFT JOIN categories c ON tp.category_id = c.category_id
        """, engine)

def right_join_products_and_categories():
    return pd.read_sql("""
        SELECT tp.testproduct_id, tp.product_name, c.category_name
        FROM testproducts tp
        RIGHT JOIN categories c ON tp.category_id = c.category_id
        """, engine)

def full_join_products_and_categories():
    return pd.read_sql("""
        SELECT tp.testproduct_id, tp.product_name, c.category_name
        FROM testproducts tp
        FULL JOIN categories c ON tp.category_id = c.category_id
        """, engine)

def cross_join_products_and_categories():
    return pd.read_sql("""
        SELECT tp.testproduct_id, tp.product_name, c.category_name
        FROM testproducts tp
        CROSS JOIN categories c
        """, engine)