from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
questions = []

for i in question_data:
    questions.append(Question(i["text"], i["answer"]))

quiz = QuizBrain(questions)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/12")
