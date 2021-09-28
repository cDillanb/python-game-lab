import random

def input_guess():
    return int(input("Your guess? "))

def loop():
    number = random.randint(1,100)
    guess = input_guess()

    for i in range(100):
        if guess > number:
            print("Your guess is too high, try again")
            guess = input_guess()
        elif guess < number:
            print("Your guess is too low, try again")
            guess = input_guess()
        else:
            return i+1
    

def main():
    player_name = input("Howdy, what's your name?\n")

    print(player_name, "I'm thinking of a number between 1 and 100.")
    print("Try to guess my number.")

    attempts = loop()
    print("Well done,", player_name, "You found my number in", attempts, "tries")


main()