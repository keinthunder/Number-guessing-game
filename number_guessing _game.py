print("🎮 Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.\n")
import random
secret_number=random.randint(1,100)
tries=0
while True:
    tries+=1
    guess=int(input('enter your number (1-100) '))
    if guess==secret_number:
        print("Congratulations! 🎉 You guessed the correct number in", tries, "tries.")
        break
    elif guess>secret_number:
        print("Too high! 📉 Try a smaller number ")
    else:
        print("Too low! 📈 Try a larger number ")
