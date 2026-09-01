questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?:"
             "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Osctrich"),
           ("A. 206", "B. 207", "C. 208", "D. "),
           ("A. ", "B. ", "C. ", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
    guess = input("Enter A, B, C or D: ").upper()
    question_num += 1