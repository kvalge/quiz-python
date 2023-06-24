from database.connect import connect
from database.create_table import create_tables

from model.topic import Topic
from model.question import Question
from model.response import Response
from model.quiz import Quiz

import pandas as pd


def add_question_to_quiz(quiz_name, question_name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO quiz_question VALUES "
                "(DEFAULT, '" + quiz_name + "', '" + question_name + "') ON CONFLICT DO NOTHING")
    cur.connection.commit()
    cur.close()


def get_question_by_topic(topic_name):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM question WHERE topic_name = '" + topic_name + "'")
    questions = cur.fetchall()
    for row in questions:
        print("{}: {}".format(topic_name, row[2]))

    cur.connection.commit()
    cur.close()


def get_questions_by_quiz(quiz_name):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT quiz_question.quiz_name, question.name "
                "FROM quiz_question "
                "INNER JOIN question "
                "ON quiz_question.question_name = question.name "
                "WHERE quiz_question.quiz_name = '" + quiz_name + "'")
    questions = cur.fetchall()
    for row in questions:
        print("{}: {}".format(quiz_name, row[1]))

    cur.connection.commit()
    cur.close()


if __name__ == '__main__':
    create_tables()

    history = Topic("History")
    music = Topic("Music")
    cinema = Topic("Cinema")
    philosophy = Topic("Philosophy")

    dataframe = pd.read_excel('data.xlsx')
    print(dataframe)

    # Reading arguments for creating Question object from data excel data file
    for i, j in dataframe.iterrows():
        Question("{}".format(dataframe.get("question_name")[i]),
                 "{}".format(dataframe.get("question_content")[i]),
                 "{}".format(dataframe.get("question_rank")[i]),
                 "{}".format(dataframe.get("topic")[i]))

    # Reading arguments for creating Response object from data excel data file
    for i, j in dataframe.iterrows():
        Response("{}".format(dataframe.get("response_content")[i]),
                 "{}".format(dataframe.get("response_correct")[i]),
                 "{}".format(dataframe.get("question_name")[i]))

    history_quiz = Quiz("History quiz")
    cinema_quiz = Quiz("Cinema quiz")

    # adding quiz and question to quiz_question table
    drop_duplicates_qq = dataframe.drop_duplicates()
    for i, j in drop_duplicates_qq.iterrows():
        add_question_to_quiz(drop_duplicates_qq.get("quiz_name")[i], drop_duplicates_qq.get("question_name")[i])

    get_question_by_topic(history.name)

    get_questions_by_quiz(history_quiz.name)
