import os
import mysql.connector
from contextlib import contextmanager
from logging_setup import logging_set
logger = logging_set('db_helper')

@contextmanager
def get_db_cursor(commit=False):
    
    # 🌟 MODIFICATION START 🌟
    # Read MySQL connection details from environment variables
    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = os.environ.get("DB_PORT", 3306) # Default MySQL port
    DB_USER = os.environ.get("DB_USER")
    DB_PASS = os.environ.get("DB_PASSWORD")
    DB_NAME = os.environ.get("DB_NAME")
    
    # Critical Check: Ensure required variables are set
    if not all([DB_HOST, DB_USER, DB_PASS, DB_NAME]):
        # Fallback to local hardcoded values only if environment variables are missing
        # This allows local testing to still work if needed
        DB_HOST = "sql209.infinityfree.com"
        DB_USER = "if0_40606242"
        DB_PASS = "WpcV4u6c7t"
        DB_NAME = "if0_40606242_expense_manager"
        
        # If we are in the cloud and fall back here, the connection will fail.
        # It's highly recommended to fail early if in a production context.
        logger.warning("Using hardcoded local database credentials. Ensure environment variables are set for cloud deployment.")
    
    connection = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    print("Closing cursor")
    cursor.close()
    connection.close()


def fetch_all_records():
    logger.info(f"fetched all data")
    query = "SELECT * from expenses"

    with get_db_cursor() as cursor:
        cursor.execute(query)
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)


def fetch_expenses_for_date(expense_date):
    logger.info(f"working")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)
        return expenses


def insert_expense(expense_date, amount, category, notes):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )


def delete_expenses_for_date(expense_date):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))

def fetch_expense_summary(start_date,end_date):
    with get_db_cursor() as cursor:
        cursor.execute('''SELECT category,sum(amount) as total FROM expenses
                          where expense_date
                          between %s and %s
                          group by category
                          ''',(start_date,end_date,))
        data = cursor.fetchall()
        return data
def fetch_summary_by_month():
    query = '''
    SELECT 
    DATE_FORMAT(MIN(expense_date), '%M %Y') AS month_year,
    
    SUM(amount) AS total_amount
    FROM 
        expenses
    GROUP BY 
        YEAR(expense_date), MONTH(expense_date)
    ORDER BY 
        YEAR(expense_date), MONTH(expense_date);
    '''
    with get_db_cursor() as cursor:
        cursor.execute(query)
        expenses = cursor.fetchall()
        return expenses
if __name__ == "__main__":
    # fetch_all_records()
    # # fetch_expenses_for_date("2024-08-01")
    # # insert_expense("2024-08-20", 300, "Food", "Panipuri")
    # delete_expenses_for_date("2024-08-20")

    # data = fetch_expense_summary("2024-08-01","2024-08-05")
    # for data in data:
    #     print(data)
    print(fetch_summary_by_month())

