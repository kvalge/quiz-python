import psycopg2
from connect import connect


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS topic (id SERIAL PRIMARY KEY, name TEXT, UNIQUE(name))
        """,
        """
        CREATE TABLE IF NOT EXISTS question 
        (id SERIAL PRIMARY KEY, content TEXT, rank INTEGER, topic_id INTEGER, UNIQUE(content))
        """,
        """
        CREATE TABLE IF NOT EXISTS response 
        (id SERIAL PRIMARY KEY, content TEXT, correct BOOLEAN, question_id INTEGER, UNIQUE(content))
        """,
        """
        CREATE TABLE IF NOT EXISTS quiz 
        (id SERIAL PRIMARY KEY, name TEXT, UNIQUE(name))
        """,
        """
        CREATE TABLE IF NOT EXISTS quiz_question 
        (id SERIAL PRIMARY KEY, quiz_id INTEGER,question_id INTEGER, UNIQUE(question_id))
        """)

    conn = None
    try:
        # connect to the PostgreSQL server
        conn = connect()
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
