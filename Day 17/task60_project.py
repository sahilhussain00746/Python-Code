from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import art

print(art.logo)
question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)
while quiz.still_have_question():
    quiz.next_question()
    

print(art.game_over_art)
print("====================================")
print("        QUIZ COMPLETED 🎉")
print("====================================")
print(f"\n        FINAL SCORE\n        -------------\n           {quiz.score} / {quiz.question_number}\n")
print("====================================")
