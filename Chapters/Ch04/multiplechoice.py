CORRECT_ANSWERS = "adbdcacbdac"

done = False
while not done :
    user_answers = input("Enter your exam answers: ")
    if len(user_answers) == len(CORRECT_ANSWERS) :
        done = True
    else:
        print("Error: an incorrect number of answers given")

num_questions = len(CORRECT_ANSWERS)
num_correct = 0
result = ""

for i in range(num_questions) :
    if user_answers[i] == CORRECT_ANSWERS[i] :
        num_correct = num_correct + 1
        result += user_answers[i]
    else :
        result+= "X"

score = round(num_correct / num_questions * 100)

if score == 100:
    print("Maximum grade")
else :
    print("You missed %d questions: %s" % (num_questions - num_correct, result))

print("Score: %d percent" % score)