import random 

num = random.randint(1,100)

attempts = 0 

print("Welcome To Number Guessing Game.!")
print("I have selected a number between 1 and 100. Can you guess it?")

while True : 
    guess = int(input("Enter The Guess:"))
    attempts += 1 
    if guess < num :
        print("Too Low! Try Again.!")
    elif guess > num :
        print("Too High! Try Again.!")
    else:
        print(f"Correct! The Number was correct {num}.")
        print(f"You Got This Number it in {attempts} attempts.")
        break