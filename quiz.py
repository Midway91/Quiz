score = (0)
name = input("What is your name? ")
print("Hello " + name)
question = input("Do you want to take a quiz? Use caps lock. ")
if question == 'NO':
    print("GET OUT OF HERE")
    print("---------------------------------------------------")
    quit()
else:
    question = input("Directions: Use caps lock for all answers or you will get it wrong, dates are written as (MONTH DAY#, YEAR) Are you ready to take the quiz? ")

    #QUESTIONS
input("First, WWII questions: Press enter")
print("When was D-Day")
answer1 = input("Answer: ")
if answer1 == 'JUNE 6, 1944':
    input("CORRECT: PRESS ENTER")
    score = score + 1
    print("Your score:")
    print(score)
else:
    input("WRONG: JUNE 6, 1944 PRESS ENTER")
    score = score - 1
    print("Your score:")
    print(score)
print("What was the name of the boat that carried the ground troops to the beaches? ")
answer2 = input("Answer: ")
if answer2 == 'HIGGINS':
    input("CORRECT: PRESS ENTER")
    score = score + 1
    print("Your score:")
    print(score)
else:
    input("WRONG: HIGGINS PRESS ENTER")
    score = score -1
    print("Your score:")
    print(score)
print("True or False: D-Day was the largest amphibious  military invasion force. ")
answer3 = input("Answer: ")
if answer3 == 'TRUE':
    input("CORRECT: PRESS ENTER")
    score = score + 1
    print("Your score:")
    print(score)
else:
    input("WRONG: TRUE PRESS ENTER")
    score = score - 1
    print("Your score")
print("What year did WWII start?")
answer4 = input("Answer: ")
if answer4 == '1939':
    input("CORRECT: PRESS ENTER")
    score = score + 1
    print("Your score")
    print(score)
else:
    input("WRONG: 1939 PRESS ENTER")
    score = score - 1
    print("Your score")
    print(score)
print("What year did America enter WWII ")
answer5 = input("Answer: ")
if answer5 == '1941':
    input("CORRECT: PRESS ENTER")
    score = score + 1
    print("Your score")
    print(score)
else:
    input("WRONG: 1941 PRESS ENTER")
    score = score - 1
    print("Your score:")
    print(score)
print("What year did WWII end? ")
answer6 = input("Answer: ")
if answer6 == '1945':
    input("CORRECT: PRESS ENTER")
    score = score + 1
    print("Your score")
    print(score)
else:
    input("WRONG: 1945 PRESS ENTER")
    score = score - 1
    print("Your score")
    print(score)
print("What date did the battle of Midway start? ")
answer7 = input("Answer: ")
if answer7 == 'JUNE 4, 1942':
    input("CORRECT: PRESS ENTER")
    score = score + 1
    print("Your score")
    print(score)
else:
    input("WRONG: JUNE 4, 1942 PRESS ENTER")
    score = score - 1
    print("Your score")
    print(score)
print("What date did the battle of Midway end? ")
answer8 = input("Answer: ")
if answer8 == 'JUNE 7, 1942':
    input("CORRECT: PRESS ENTER")
    score = score + 1
    print("Your score")
    print(score)
else:
    input("WRONG: JUNE 7, 1942 PRESS ENTER")
    score = score - 1
    print("Your score")
    print(score)
print("Who won the battle of Midway? ")
answer9 = input("Answer: ")
if answer9 == 'AMERICA':
    input("CORRECT: PRESS ENTER")
    score = score + 1
    print("Your score")
    print(score)
else:
    input("WRONG: AMERICA PRESS ENTER")
    score = score - 1
    print("Your score")
    print(score)
print("What was the name of the airplane that dropped the atomic bomb? ")
answer10 = input("Answer: ")
if answer10 == 'ENOLA GAY':
    input("CORRECT: PRESS ENTER")
    score = score + 1
    print("Your score")
    print(score)
else:
    input("WRONG: ENOLA GAY PRESS ENTER")
    score = score - 1
    print("Your score")
    print(score)
input("That ends the WWII questions. PRESS ENTER")
input("Now for the general knowledge questions. PRESS ENTER")

#GENERAL KNOWLEDGE QUESTIONS
input("Ready for the general knowledge questions? PRESS ENTER")
print("What year did Ohio become a state? ")
answer11 = input("Answer: ")
if answer11 == '1803':
    input("CORRECT: PRESS ENTER")
    score = score + 1
    print("Your score")
    print(score)
else:
    input("WRONG: 1803 PRESS ENTER")
    score = score - 1
    print("Your score")
    print(score)
print("Who was the first president? ")
answer12 = input("Answer: ")
if answer12 == 'GEORGE WASHINGTON':
    input("CORRECT: PRESS ENTER")
    score = score + 1
    print("Your score")
    print(score)
else:
    input("WRONG: GEORGE WASHINGTON, PRESS ENTER")
    score = score - 1
    print("Your score")
    print(score)
print("Who was the 30th president? ")
answer13 = input("Answer: ")
if answer13 == 'CALVIN COOLIDGE':
    input("CORRECT: PRESS ENTER")
    score = score + 1
    print("Your score")
    print(score)
else:
    input("WRONG: CALVIN COOLIDGE, PRESS ENTER")
    score = score - 1
    print("Your score")
    print(score)
print("The Manhattan project created what? ")
answer14 = input("Answer: ")
if answer14 == 'THE ATOMIC BOMB':
    input("CORRECT: PRESS ENTER")
    score = score + 1
    print("Your score")
    print(score)
else:
    input("WRONG: THE ATOMIC BOMB, PRESS ENTER")
    score = score - 1
    print("Your score")
    print(score)
print("This is the end of the quiz yout score is: ")
print(score)
quit()