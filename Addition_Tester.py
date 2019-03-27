#addition_tester.py
import random
num1 = random.randint(1, 5)    #line 3 and 4 generates 2 random numbers to ask the user to add
num2 = random.randint(1, 5)
print(f"What is {num1} + {num2}")

while True:

    user_answer = input("Your answer: ")
    user_answer = int(user_answer)

    if user_answer == num1 + num2:
        print("Correct!")
        break
    else:
        print("Try again")
