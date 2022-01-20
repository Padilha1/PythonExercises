print ("Welcome to the Quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay, let's play :) ")
score = 0

answer = input ("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct! ')
    score += 1
else: 
    print("Incorrect! ")

answer = input ("AI gonna be more experts than us? ")
if answer.lower() == "yes":
    print('Correct! ')
    score += 1
else: 
    print("Incorrect! ")

answer = input ("Save a dog or a cat? ")
if answer.lower() == "dog":
    print('Correct! ')
    score += 1
else: 
    print("Incorrect! ")

answer = input (" What does RAM means ? ")
if answer.lower() == "random access memory":
    print('Correct! ')
    score += 1
else: 
    print("Incorrect! ")

print ("You  got " + str(score) + " questions correct! ")
print ("You  got " + str((score/4) * 100) + "% ")
