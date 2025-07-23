 # Create a mini Python quiz that takes answers from the user and displays score.
import random
import cowsay
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "correct": "C"
    },  
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "correct": "B"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A. O2", "B. H2O", "C. CO2", "D. NaCl"],
        "correct": "B"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. William Wordsworth", "B. Charles Dickens", "C. William Shakespeare", "D. Mark Twain"],
        "correct": "C"
    },
    {
        "question": "What is the largest mammal on the earth?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Polar Bear"],
        "correct": "B"
    },
]

random.shuffle(questions)
def main():
    print("Lets play Kaun banega crorepati!")
    name=input("Enter your name")
    print("Here are the questions")
    Askquestion(questions)
    print(f"Thankyou {name} for playing KBC")

def Askquestion(questions):
    count=0     
    for i,q in enumerate(questions):
        print(f"Q{i+1} {q['question']}")
        for option in q['options']:
            print(option)            
        try:
            print()
            answer=input("Enter your answer in A , B , C , D").title()            
            if answer == q['correct']:
                print("Correct!")
                count+=1
                if count==5:
                    cowsay.dragon("Congratulations!You are a crorepati!")
                    return                     
            else:   
                cowsay.pig(f'''Incorrect,See u Next time !''')
                print(f"Here is your amount {count*1000000}")
                return
        except ValueError: 
                print("Invalid value")
main()