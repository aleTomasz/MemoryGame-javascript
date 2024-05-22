from psycopg.sql import SQL
import database_common
import bcrypt

@database_common.connection_handler
def add_user(cursor, login, user_password):
    hashed_password = bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt())
    cursor.execute(
        SQL("INSERT INTO users (login, password) VALUES (%(login)s, %(user_password)s) RETURNING id"),
        {'login': login, 'user_password': hashed_password.decode('utf-8')}
    )
    return cursor.fetchone()['id']

@database_common.connection_handler
def get_user(cursor, login, user_password):
    cursor.execute(
        SQL("SELECT * FROM users WHERE login = %(login)s"),
        {'login': login}
    )
    user = cursor.fetchone()
    if user and bcrypt.checkpw(user_password.encode('utf-8'), user['password'].encode('utf-8')):
        return user
    return None