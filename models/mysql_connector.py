import mysql.connector as db
from dotenv import load_dotenv
import os

# load all environment variable here
load_dotenv()

# all database values
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB = os.getenv("DB")

database_config = {
    "user": DB_USER,
    "password": DB_PASSWORD,
    "host": DB_HOST,
    "database": DB,
}


def mysql_database_connection(func):
    def wrapper(*args, **kwargs):
        try:
            # create connection to mysql
            conn = db.connect(**database_config)
            cursor = conn.cursor()
            print("database connection ===========")
            return func(*args, **kwargs, database=conn, cursor=cursor)
        except db.Error as err:
            print("database connection error: ", err)
        finally:
            print("database closing ==============")
            cursor.close()
            conn.close()
        return None

    return wrapper
