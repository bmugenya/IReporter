import psycopg2

url = "dbname='IReporter' user='postgres' host='localhost' port=5433 password='Boywonder47'"


class database_setup(object):

    def __init__(self):
        self.conn = psycopg2.connect(url)
        self.cursor = self.conn.cursor()

    def destroy_tables(self):
        self.cursor.execute("""DROP TABLE IF EXISTS Users CASCADE;""")
        self.cursor.execute("""DROP TABLE IF EXISTS Posts CASCADE;""")

        self.conn.commit()

    def create_tables(self):

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Users (
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

            );""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Posts (
            id SERIAL,
            createdOn timestamp ,
            createdBy    SERIAL,
            post_type       VARCHAR(25)    NOT NULL,
            location   VARCHAR(50)    NOT NULL,
            status   VARCHAR(25)   NOT NULL,
            photo    VARCHAR(25),
            video        VARCHAR(25),
            comments  VARCHAR(250) NOT NULL
            );""")

        self.conn.commit()
