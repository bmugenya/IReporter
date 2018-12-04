"""Class to set up application database"""
import psycopg2
import os

url = "dbname='IReporter', user='postgres', password='Qw12Er34', host='localhost', port='5432'"

db_url = os.getenv('DATABASE_URL')


def connection(url):
    con = psycopg2.connect(url)
    return con


def init_db():
    con = connection(url)
    return con


def create_tables():
    conn = connection(url)
    c = conn.cursor()
    queries = tables()

    for query in queries:
        c.execute(query)
    conn.commit()


def destroy_tables():
    db1 = """DROP TABLE IF EXISTS flag CASCADE"""
    pass


def tables(self):
    db1 = """CREATE TABLE IF NOT EXISTS flag(
        id          SERIAL PRIMARY KEY,
        title       VARCHAR(50)    UNIQUE NOT NULL,
        type    VARCHAR(100)   NOT NULL,
        location        VARCHAR(10)    NOT NULL,
        incident        VARCHAR(10)    NOT NULL,
        created_at  VARCHAR(50)
        );"""

    queries = [db1]
    return queries

    # save_user_sql = """INSERT INTO users(email, password, role, created_at)
    #                   VALUES(%(email)s, %(password)s, %(role)s, %(created_at)s);"""
    self.database_connection.commit()
    self.cursor.close()
    self.database_connection.close()
