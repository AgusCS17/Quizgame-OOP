from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

Question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_difficult = question["difficulty"]
    new_question = Question(question_text,question_answer,question_difficult)
    Question_bank.append(new_question)

quiz = QuizBrain(Question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
print(f"Your final point is: {quiz.point}")