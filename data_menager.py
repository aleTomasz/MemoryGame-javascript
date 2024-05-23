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

@database_common.connection_handler
def set_score(cursor, id, score):
    cursor.execute(
        SQL("UPDATE users SET rank = %(score)s WHERE id = %(id)s"),
        {'score': score, 'id': id})

@database_common.connection_handler
def ranking(cursor):
    cursor.execute(
        SQL("SELECT login, rank FROM users ORDER BY rank ASC LIMIT 10")
    )
    return cursor.fetchall()
