import random
from question import Question
import sqlite3


class Quiz:

    def __init__(self, title):
        self.title = title
        self.used_questions = []
        self.answers = []
        self.correct = 0

    def generate_new_quiz(self):
        self.correct = 0
        self.answers.clear()
        self.used_questions.clear()

        connection = sqlite3.connect('quiz.db')
        cursor = connection.cursor()

        for i in range(1, 6):
            cursor.execute(f'''SELECT count(*) FROM questions WHERE category=={i}''')
            connection.commit()
            row_num = cursor.fetchone()[0]
            cursor.execute(f"SELECT * FROM questions WHERE category=={i}")
            connection.commit()
            question = cursor.fetchall()[random.randint(0, row_num - 1)]
            new_question = Question(str(question[0]), str(question[1]))
            new_question.add_answer(str(question[2]))
            new_question.add_answer(str(question[3]))
            new_question.add_answer(str(question[4]))
            self.used_questions.append(new_question)
        connection.close()

    def add_answer(self, question, answer):
        self.answers.append([question, answer])
        if question.right_answer == answer:
            self.correct += 1



