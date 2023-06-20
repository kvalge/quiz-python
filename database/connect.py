import psycopg2


def connect():
    conn = None
    try:
        conn = psycopg2.connect(database="quiz-python",
                                host="localhost",
                                user="postgres",
                                password="postgres",
                                port="5432")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return conn
