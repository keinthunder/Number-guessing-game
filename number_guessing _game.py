print("🎮 Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.\n")
import random
secret_number=random.randint(1,100)
Tries=0
while True:
    Tries+=1
    guess=int(input('enter your number between 1-100'))
    if Hum==a:
        print("Congratulations! 🎉 You guessed the correct number in", Tries, "tries.")
        break
    elif Hum>a:
        print("Too high! 📉 Try a smaller number")
    else:
        print("Too low! 📈 Try a larger number")
