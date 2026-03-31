# PostgreSQL Practice Repository

A beginner practice project for connecting **Python** with **PostgreSQL** and executing SQL queries using existing relational tables such as customers, products, and categories.

## Purpose

This repository is used to practice:

* Connecting Python to PostgreSQL
* Writing SQL queries inside Python
* Executing JOIN operations
* Fetching and displaying results
* Organizing database code using a clean project structure

## Technologies Used

* Python 3
* PostgreSQL
* psycopg
* python-dotenv

## Project Structure

```bash
project/
│── main.py
│── db.py
│── queries.py
│── config.py
│── .env
│── .gitignore
│── requirements.txt
│── README.md
```

## File Responsibilities

* `main.py` → program entry point
* `db.py` → database connection
* `queries.py` → SQL queries and reusable functions
* `config.py` → environment variable loading

## Example SQL Concepts To Be Practiced

* SELECT
* WHERE
* ORDER BY
* INNER JOIN
* GROUP BY
* INSERT
* UPDATE
* DELETE

## Example Query

```sql
SELECT p.product_name, c.category_name
FROM products p
INNER JOIN categories c
ON p.category_id = c.category_id;
```

## Learning Notes

This project is focused on improving understanding of relational databases before moving into web frameworks such as Flask and Django.

## Future Improvements

* Add CRUD menu system
* Add parameterized user input
* Add reusable query modules
* Convert into Flask web app
