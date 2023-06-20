from database.create_table import create_tables
from model.topic import Topic
from model.question import Question

if __name__ == '__main__':
    create_tables()

    history = Topic("History")
    music = Topic("Music")
    cinema = Topic("Cinema")
    philosophy = Topic("Philosophy")

    q1 = Question("Which country was known as Rhodesia before gaining independence from the British in 1979?",
                  "2",
                  "History")

    q2 = Question("Which country was unified by Giuseppe Garibaldi in 1851?",
                  "2",
                  "History")

    q3 = Question("Which President was brought down by the Watergate Scandal?",
                  "2",
                  "History")

    q4 = Question("Who directed Lost in Translation?",
                  "2",
                  "Cinema")
