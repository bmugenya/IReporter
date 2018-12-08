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
    db1 = """CREATE TABLE IF NOT EXISTS Posts (
        id SERIAL PRIMARY KEY,
        createdOn timestamp with time zone DEFAULT ('now'::text)::date NOT NULL,
        createdBy    SERIAL,
        incident       VARCHAR(25)    NOT NULL,
        location   VARCHAR(50)    NOT NULL,
        status   VARCHAR(25)   NOT NULL,
        photo    VARCHAR(25),
        video        VARCHAR(25),
        comments  VARCHAR(250) NOT NULL
        );"""

    queries = [db1]
    return queries
