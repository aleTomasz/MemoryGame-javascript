import os
from datetime import datetime
import psycopg
from psycopg import sql
from datetime import datetime
from psycopg.sql import SQL
import database_common

# @database_common.connection_handler
# def add_user(cursor, login, user_password):
#     return cursor.execute(
#         SQL("INSERT INTO users (login, password) values (%(login)s, %(user_password)s, returning id"),
#         {'user_login': login, 'user_password': user_password}).fetchone()['id']

# propozycja
@database_common.connection_handler
def add_user(cursor, login, user_password):
    cursor.execute(
        SQL("INSERT INTO users (login, password) VALUES (%(login)s, %(user_password)s) RETURNING id"),
        {'login': login, 'user_password': user_password}
    )
    return cursor.fetchone()['id']

@database_common.connection_handler
def get_user(cursor, login, user_password):
    cursor.execute(
        SQL("SELECT * FROM users WHERE login = %(login)s AND password = %(user_password)s"),
        {'login': login, 'user_password': user_password}
    )
    return cursor.fetchone()
