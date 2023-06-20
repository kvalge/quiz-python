from database.connect import connect


class Question:

    def __init__(self, name, content, rank, topic_name):
        self.name = name
        self.content = content
        self.rank = rank
        self.topic_name = topic_name

        conn = connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO question VALUES "
            "(DEFAULT, '" + name + "','" + content + "', '" + rank + "', '" + topic_name + "') ON CONFLICT DO NOTHING")
        cur.connection.commit()
        cur.close()
