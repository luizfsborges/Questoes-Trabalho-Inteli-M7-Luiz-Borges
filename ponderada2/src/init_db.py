# init_db.py

import psycopg2
import time

def wait_for_postgresql(max_retries=30, retry_interval=1):
    for _ in range(max_retries):
        try:
            psycopg2.connect(
                dbname='notes_db',
                user='your_username',
                password='your_password',
                host='database',
                port=5432
            )
            print("PostgreSQL is ready.")
            return
        except psycopg2.OperationalError as e:
            print(f"Waiting for PostgreSQL: {e}")
            time.sleep(retry_interval)

    raise Exception("Timed out waiting for PostgreSQL to start.")

wait_for_postgresql()

# Your database initialization code here
# For example:
# - Creating tables
# - Inserting initial data
