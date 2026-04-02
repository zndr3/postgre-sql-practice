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

def union_products_and_testproducts():
    return pd.read_sql("""
        SELECT product_id, product_name
        FROM products
        UNION
        SELECT testproduct_id, product_name
        FROM testproducts
        ORDER BY product_id;
        """, engine)

def union_all_products_and_testproducts():
    return pd.read_sql("""
        SELECT product_id, product_name
        FROM products
        UNION ALL
        SELECT testproduct_id, product_name
        FROM testproducts
        ORDER BY product_id;
        """, engine)

def inner_join_customer_names_with_orders():
    return pd.read_sql("""
        SELECT c.customer_name AS "Customer Names", p.product_name AS "Ordered Products"
        FROM products p
        INNER JOIN order_details od
        ON od.product_id = p.product_id
        INNER JOIN orders o
        ON od.order_id = o.order_id
        INNER JOIN customers c
        ON o.customer_id = c.customer_id;
        """, engine)

def total_bill_per_customer():
    return pd.read_sql("""
        SELECT c.customer_name AS "Customer Names", p.product_name AS "Product Name",
        p.unit AS "Product Unit", p.price AS "Product Price", od.quantity,
        SUM(p.price * od.quantity) AS "Total Bill"
        FROM products p
        INNER JOIN order_details od
        ON od.product_id = p.product_id
        INNER JOIN orders o
        ON od.order_id = o.order_id
        INNER JOIN customers c
        ON o.customer_id = c.customer_id
        GROUP BY c.customer_name, p.product_name, p.unit, p.price, od.quantity
        ORDER BY c.customer_name;
        """, engine)

def bill_above_1000():
    return pd.read_sql("""
        SELECT c.customer_name AS "Customer Names", p.product_name AS "Product Name",
        p.unit AS "Product Unit", p.price AS "Product Price", od.quantity,
        SUM(p.price * od.quantity) AS "Total Bill"
        FROM products p
        INNER JOIN order_details od
        ON od.product_id = p.product_id
        INNER JOIN orders o
        ON od.order_id = o.order_id
        INNER JOIN customers c
        ON o.customer_id = c.customer_id
        GROUP BY c.customer_name, p.product_name, p.unit, p.price, od.quantity
        HAVING SUM(p.price * od.quantity) >= 1000
        ORDER BY c.customer_name;
        """, engine)

def exist_customer_with_orders():
    return pd.read_sql("""
        SELECT c.customer_name
        FROM customers c
        WHERE EXISTS (
        SELECT 1
        FROM orders o
        WHERE o.customer_id = c.customer_id
        )
        """, engine)

def not_exist_customer_without_orders():
    return pd.read_sql("""
        SELECT c.customer_name
        FROM customers c
        WHERE NOT EXISTS (
        SELECT 1
        FROM orders o
        WHERE o.customer_id = c.customer_id
        )
        """, engine)