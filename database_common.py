import os
import psycopg
import psycopg.rows


def get_connection_string():
    user_name = os.environ.get('PSQL_USER_NAME')
    password = os.environ.get('PSQL_PASSWORD')
    host = os.environ.get('PSQL_HOST')
    database_name = os.environ.get('PSQL_DB_NAME')
    port = os.environ.get('PSQL_PORT')

    env_variables_defined = user_name and password and host and database_name

    if env_variables_defined:

        return f'postgresql://{user_name}:{password}@{host}:{port}/{database_name}'
    else:
        raise KeyError('Some necessary environment variable(s) are not defined')


def open_database():
    try:
        connection_string = get_connection_string()
        connection = psycopg.connect(connection_string)
        connection.autocommit = True
    except psycopg.DatabaseError as exception:
        print('Database connection problem')
        raise exception
    return connection


def connection_handler(function):
    def wrapper(*args, **kwargs):
        with open_database() as connection:
            with connection.cursor(row_factory=psycopg.rows.dict_row) as cursor:
                ret_value = function(cursor, *args, **kwargs)

        return ret_value

    return wrapper
