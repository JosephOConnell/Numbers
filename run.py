import random
import os
import sys
from time import sleep


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

        print(f"You got {score} out of 5")
        print("--------------------------")

    def subtraction():
        score = 0
        print("Subtraction Maths")
        for i in range(5):
            num1 = random.randint(5, 10)
            num2 = random.randint(1, 5)
            result = num1 - num2

            guess_input = input(f"What is {num1} - {num2} = ")
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

        print(f"You got {score} out of 5")
        print("--------------------------")

    def addition_and_subtraction():
        score = 0
        print("Addition and Subtraction Maths")

        for i in range(5):
            num1 = random.randint(1, 5)
            num2 = random.randint(1, 5)
            num3 = random.randint(1, 5)
            result = num1 + num2 - num3

            guess_input = input(f"What is {num1} + {num2} - {num3} = ")
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

        print(f"You got {score} out of 5")
        print("--------------------------")

    print("Welcome to Maths Questions")
    choice_input = input(
        "Please choose" +
        "\n1 = Addition" +
        "\n2 = Subtraction" +
        "\n3 = Addition and Subtraction \n")
    choice_input = int(choice_input)

    if choice_input == 1:
        addition()
    elif choice_input == 2:
        subtraction()
    elif choice_input == 3:
        addition_and_subtraction()
    else:
        random_maths_quiz()


def higher_lower():
    """
    Higher and Lower Game.
    """
    print("Welcome to Higher or Lower")
    tries = 0
    num = random.randint(1, 50)
    while True:
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
        main()

    elif play_again_input == "n":
        print("Thanks for Playing")

    else:
        print("Please choose Y or N")
        play_again()


def main():
    """
    Main Function
    """
    print("Please pick a game")
    choice_input = input(
        "Please choose \n1 = Simple Maths \n2 = Higher or Lower \n")
    choice_input = int(choice_input)
    if choice_input == 1:
        random_maths_quiz()
    elif choice_input == 2:
        higher_lower()
    else:
        print("Something went wrong")
        main()


main()
