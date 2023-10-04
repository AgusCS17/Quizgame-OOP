class QuizBrain:

    def __init__(self,q_list):
        self.question_number = 0
        self.list = q_list
        self.score = 0
        self.point = 0

    def still_has_question(self):
        return self.question_number < len(self.list)


    def next_question(self):
        current_question = self.list[self.question_number]
        self.question_number += 1
        print(f"Your point: {self.point}")
        print(f"Difficult: {current_question.difficult}")
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer,current_question.answer, current_question.difficult)


    def check_answer(self, user_answer, correct_answer,difficult):
        current_question = self.list[self.question_number]
        if user_answer.lower() == correct_answer.lower() and difficult == "easy":
            self.point += 10
            self.score += 1
            print("You got it right")
        elif user_answer.lower() == correct_answer.lower() and difficult == "medium":
            self.point += 30
            self.score += 1
            print("You got it right")
        elif user_answer.lower() == correct_answer.lower() and difficult == "hard":
            self.point += 50
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong answer.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")




