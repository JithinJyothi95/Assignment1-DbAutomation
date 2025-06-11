# deploy_changes_script.py

import mysql.connector
from mysql.connector import errorcode

DB_NAME = "prog8850_db"
SQL_FILE = "schema_changes.sql"

config = {
    'user': 'root',
    'password': 'Secret5555',
    'host': '127.0.0.1'
}

def create_database(cursor):
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print(f" Database '{DB_NAME}' is ready.")
    except mysql.connector.Error as err:
        print(f" Failed creating database: {err}")
        exit(1)

def apply_sql_file(cursor, file_path):
    try:
        with open(file_path, 'r') as f:
            sql_commands = f.read().split(';')
            for command in sql_commands:
                if command.strip():
                    cursor.execute(command)
        print("Schema changes applied.")
    except FileNotFoundError:
        print("SQL file not found.")
    except mysql.connector.Error as err:
        print(f"SQL execution error: {err}")

try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    create_database(cursor)
    cnx.database = DB_NAME
    apply_sql_file(cursor, SQL_FILE)
    cnx.commit()
    cursor.close()
    cnx.close()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Access denied: Check user/password.")
    else:
        print(err)
