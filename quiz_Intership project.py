#Define a list for Question,Option and Correct Answer
quiz_data=[
    {
        'question':'What currency of Japan?',
        'options':['A. Won','B. Yen','C. Yuan','D. Ringgit'],
        'correct_Answer':'B'
    },
    {
        'question':'Who is the greatest Athlete of all time ?',
        'options':['A. Michell Jorden','B. Ussain Bolt','C. Cristiano Ronaldo','D. Lionel messi'],
        'correct_Answer':'A'
},
{
    'question':'Who painted the Mona Lisa ?',
        'options':['A. Leonardo da vinci','B. Vincent van Gogh','C. Pablo picasso','D. Claude Monet'],
        'correct_Answer':'A'
}
# Here You Can Add Another Questions For the Quiz
]

#initilize score 
score=0
# Display of question and Input 

def display_question(question_data):
    print(question_data['question'])
    for option in question_data['options']:
        print(option)
    user_answer = input("Your Answer:").upper()
    return user_answer
    
def evaluate_answer(user_answer, correct_answer):
    global score
    if user_answer == correct_answer:
        print("Correct!\n")
        score += 1
    else:
        print(f"incorrect. the correct answer is {correct_answer}.\n")

def display_final_score():
    print(f"your final score is: {score}/{len(quiz_data)}")


#main quiz loop
   
for question_data in quiz_data:
    user_answer = display_question(question_data)
    evaluate_answer(user_answer, question_data['correct_Answer'])


#display final score
display_final_score()


