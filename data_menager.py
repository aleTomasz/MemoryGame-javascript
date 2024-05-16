import os
from datetime import datetime
import psycopg
from psycopg import sql
from datetime import datetime
from psycopg.sql import SQL
import database_common

@database_common.connection_handler
def add_user(cursor, login, user_password):
    return cursor.execute(
        SQL("INSERT INTO users (login, password) values (%(login)s, %(user_password)s, returning id"),
        {'user_login': login, 'user_password': user_password}).fetchone()['id']


