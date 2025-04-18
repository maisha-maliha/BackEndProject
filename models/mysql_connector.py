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
        conn = None
        try:
            # if connection with database(DB) doesnt exist then we create it
            if not conn:
                temp_connection = db.connect(
                    user=DB_USER, password=DB_PASSWORD, host=DB_HOST
                )
                temp_cursor = temp_connection.cursor()
                temp_cursor.execute("SHOW DATABASES")
                databases = [x[0] for x in temp_cursor.fetchall()]

                # check if database exists or not
                if DB not in databases:
                    temp_cursor.execute(f"CREATE DATABASE {DB}")
                temp_cursor.close()
                temp_connection.close()

            # create connection to mysql with our database DB
            conn = db.connect(**database_config)
            cursor = conn.cursor()
            print("database connected ===========")

            return func(*args, **kwargs, database=conn, cursor=cursor)

        except db.Error as err:
            print("database connection error: ", err)
        finally:
            print("database closing ==============")
            cursor.close()
            conn.close()
        return None

    return wrapper
