from data import question_data, logo
from question_model import Question
from quiz_brain import QuizBrain

print(logo)
question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_have_question():
    quiz.next_question()

print("You've completed the quiz.👏")
print(f"Your final score is: {quiz.score}/{quiz.question_number} 📝")