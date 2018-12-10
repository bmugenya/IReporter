import psycopg2

url = "dbname='IReporter' user='postgres' host='localhost' port=5433 password='Boywonder47'"


def connection(url):
    con = psycopg2.connect(url)
    return con


def init_db():
    con = connection(url)
    return con


def create_tables():
    conn = init_db()
    c = conn.cursor()
    queries = tables()

    for query in queries:
        c.execute(query)
    conn.commit()


def destroy_tables():
    # db1 = """DROP TABLE IF EXISTS Posts CASCADE"""
    pass


def tables():

    db1 = """CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        firstname VARCHAR(25) NOT NULL,
        lastname  VARCHAR(25) NOT NULL,
        othernames VARCHAR(25),
        email       VARCHAR(25)    NOT NULL,
        phoneNumber  VARCHAR(50)    NOT NULL,
        username   VARCHAR(25)   NOT NULL,
        register  VARCHAR(25),
        isAdmin   VARCHAR(25),
        password VARCHAR(255) NOT NULL

        );"""

    db2 = """CREATE TABLE IF NOT EXISTS Posts (
        post_id INTEGER,
        createdOn timestamp with time zone DEFAULT ('now'::text)::date NOT NULL,
        createdBy    SERIAL,
        post_type       VARCHAR(25)    NOT NULL,
        location   VARCHAR(50)    NOT NULL,
        status   VARCHAR(25)   NOT NULL,
        photo    VARCHAR(25),
        video        VARCHAR(25),
        comments  VARCHAR(250) NOT NULL,
        FOREIGN KEY (post_id) REFERENCES Users (id)
        );"""

    queries = [db1, db2]
    return queries
