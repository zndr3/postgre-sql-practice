# SQL Practice
# JOIN practice
# GROUP BY practice


from db import get_connection

def show_products_with_categories():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT p.product_name, c.category_name
        FROM products p
        INNER JOIN categories c
        ON p.category_id = c.category_id
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def show_customers():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customers")

    rows = cursor.fetchall()

    conn.close()

    return rows