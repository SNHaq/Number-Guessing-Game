from random import Random
number = Random.Random(0, 5)
guess1 = input("Please input your first guess here: ")
guess2 = input("Please input your second guess here: ")
guess3 = input("Please input your third guess here: ")
guess4 = input("Please input your fourth guess here: ")
guess5 = input("Please input your fifth guess here: ")
chances = 5

while chances <= 5: 
    if guess1 + 50 or guess1 - 50 <= number :
        print("You're guess was 50 numbers or less away from the number!")
    else:
        print("You're not to close to the answer. :(")
    if guess1 == number:
        print("Congratulations, you won!!!")
    else:
        chances = chances - 1
        print("You have ", chances, " remaining.")
        if guess2 == number:
            print("Congratulations, you won!!!")
        else:
            chances = chances - 1
            print("You have ", chances, " remaining.")
            if guess3 == number:
                print("Congratulations, you won!!!")
            else:
                chances = chances - 1
                print("You have ", chances, " remaining.")
                if guess4 == number:
                    print("Congratulations, you won!!!")
                else:
                    chances = chances - 1
                    print("You have ", chances, " remaining.")
                    if guess5 == number:
                        print("Congratulations, you won!!!")
                    else: 
                        print("You lost! The number was: ", number)