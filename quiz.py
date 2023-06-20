from database.create_table import create_tables
from model.topic import Topic

if __name__ == '__main__':
    create_tables()
    history = Topic("History")
    music = Topic("Music")
    cinema = Topic("Cinema")
    philosophy = Topic("Philosophy")