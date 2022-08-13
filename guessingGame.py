import random
print("Welcome to the Number Guessing Game!")
num = random.randint(0, 10)
triesLeft = 0
print("Guess a number between 0 and 10!")

while triesLeft < 5: 
    guess = int(input("Enter your guess here: "))
    if guess == num: 
        print("Congratulations, you've won the game!")
        break
    elif guess < num: 
        print("Just a little higher! You're last guess was ", guess, ".")
    else: 
        print("That's a little too high, try guessing something lower! You're last guess was ", guess, ".")
    triesLeft += 1
    #This checks to see whether or not you've already used your 5 guesses. 
    if not triesLeft < 5: 
        print("You lost this time, but good try! The number was ", num, "!")
