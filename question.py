import random


class Question:

    def __init__(self, question, right_answer):
        self.line = question
        self.right_answer = right_answer
        self.answers = ['', '', '', '']
        self.answers[random.randint(0, len(self.answers) - 1)] = right_answer

    def add_answer(self, new_answer):
        if self.answers.count(new_answer) == 0:
            for i in range(0, len(self.answers)):
                if self.answers[i] == '':
                    self.answers[i] = new_answer
                    break

    def get_emoji(self, answer):
        if answer == self.right_answer:
            return 'Correct ✔'
        else:
            return 'Incorrect ❌'