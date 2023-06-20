from database.connect import connect


class Topic:

    def __init__(self, name):
        self.name = name

        conn = connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO topic VALUES (DEFAULT, '" + name + "')")
        cur.connection.commit()
        cur.close()

    def return_id(self, topic_name):
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT id FROM topic WHERE name = '" + topic_name + "'")
        cur.connection.commit()
        cur.close()
