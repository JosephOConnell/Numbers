import random
import os
import sys
from time import sleep
"""
random to randomise the numbers in the quiz and higher/lower game
os to clear the terminal of text
sys for system exit
sleep to give a slight pause in between code
"""


def random_maths_quiz():
    """
    Maths questions.
    Addition, Subtraction and Both.
    """
    def addition():
        score = 0
        print("Addition Maths")
        for i in range(5):
            num1 = random.randint(1, 5)
            num2 = random.randint(1, 5)
            result = num1 + num2
            guess_input = input(f"What is {num1} + {num2} = ")
            try:
                guess_input = int(guess_input)
                if guess_input == result:
                    print("CORRECT")
                    print("---------------------")
                    score += 1
                elif guess_input != result:
                    print("WRONG")
                    print("---------------------")
                else:
                    print("Something went wrong")
                    print("---------------------")
            except ValueError:
                i += 1
                print("WRONG")
                print("Please pick a number")   
                print("---------------------")

        print(f"You got {score} out of 5")
        print("--------------------------")
        play_again()

    def subtraction():
        score = 0
        print("Subtraction Maths")
        for i in range(5):
            num1 = random.randint(5, 10)
            num2 = random.randint(1, 5)
            result = num1 - num2

            guess_input = input(f"What is {num1} - {num2} = ")
            try:
                guess_input = int(guess_input)

                if guess_input == result:
                    print("CORRECT")
                    print("---------------------")
                    score += 1
                elif guess_input != result:
                    print("WRONG")
                    print("---------------------")
                else:
                    print("Something went wrong")
                    print("---------------------")
            except ValueError:
                i += 1
                print("WRONG")
                print("Please pick a number")   
                print("---------------------")

        print(f"You got {score} out of 5")
        print("--------------------------")
        play_again()

    def addition_and_subtraction():
        score = 0
        print("Addition and Subtraction Maths")

        for i in range(5):
            num1 = random.randint(1, 5)
            num2 = random.randint(1, 5)
            num3 = random.randint(1, 5)
            result = num1 + num2 - num3

            guess_input = input(f"What is {num1} + {num2} - {num3} = ")
            try:
                guess_input = int(guess_input)

                if guess_input == result:
                    print("CORRECT")
                    print("---------------------")
                    score += 1
                elif guess_input != result:
                    print("WRONG")
                    print("---------------------")
                else:
                    print("Something went wrong")
                    print("---------------------")
            except ValueError:
                i += 1
                print("WRONG")
                print("Please pick a number")   
                print("---------------------")

        print(f"You got {score} out of 5")
        print("--------------------------")
        play_again()

    print("Welcome to Maths Questions")
    choice_input = input(
        "Please choose" +
        "\n1 = Addition" +
        "\n2 = Subtraction" +
        "\n3 = Addition and Subtraction \n")
    choice_input = int(choice_input)

    if choice_input == 1:
        os.system('clear')
        addition()
    elif choice_input == 2:
        os.system('clear')
        subtraction()
    elif choice_input == 3:
        os.system('clear')
        addition_and_subtraction()
    else:
        os.system('clear')
        random_maths_quiz()


def higher_lower():
    """
    Higher and Lower Game.
    """
    print("Welcome to Higher or Lower")
    tries = 0
    num = random.randint(1, 50)
    while True:
        try:
            num_input = input(f'Choose a number between 1 - 50\n')
            num_input = int(num_input)
            if num_input == num:
                print("Correct")
                print("---------------------")
                tries += 1
                break
            elif num_input > num:
                print("Too High")
                print("---------------------")
                tries += 1
            elif num_input < num:
                print("Too Low")
                print("---------------------")
                tries += 1
            else:
                print("Something went wrong pick again")
                print("---------------------")
        except ValueError:
            print("Please pick a number")

    print(f'It took you {tries} tries to get the number')
    print("--------------------------")
    play_again()


def play_again():
    """
    Play Again Function.
    """
    play_again_input = input(
        "Would you like to play another game?\nY/N\n").lower()
    if play_again_input == "y":
        sleep(1)
        os.system('clear')
        main()

    elif play_again_input == "n":
        print("Thanks for Playing")
        sleep(2)
        os.system('clear')
        sys.exit(0)

    else:
        print("Please choose Y or N")
        play_again()


def main():
    """
    Main Function
    """
    while True:
        try:
            os.system('clear')
            print("Please pick a game")
            choice_input = input(
                "Please choose \n1 = Simple Maths \n2 = Higher or Lower \n3 = Exit Terminal \n")
            choice_input = int(choice_input)
            if choice_input == 1:
                os.system('clear')
                random_maths_quiz()
            elif choice_input == 2:
                os.system('clear')
                higher_lower()
            elif choice_input == 3:
                os.system('clear')
                sys.exit(0)
            else:
                print("Something went wrong")
                sleep(1.5)
                main()

        except ValueError:
            print("Please pick a number")
            sleep(2)


main()
