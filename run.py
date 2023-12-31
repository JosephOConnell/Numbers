import random
import operator
import os
import sys
from time import sleep
import gspread
from google.oauth2.service_account import Credentials
import pyfiglet

"""
random to randomise the numbers in the quiz and higher/lower game.
Python operator module is one of the inbuilt modules in Python.
os to clear the terminal of text.
sys for system exit.
sleep to give a slight pause in between code.
gspread is a library designed for working with Google Spreadsheets.
credentials is used to access the resources offered by Google APIs.
pyfiglet is ASCII text and renders it in ASCII art fonts.
"""

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('number_facts')


def random_maths_quiz():
    """
    Maths questions for Addition, Subtraction and Multiplication.
    Runs a for loop through 5 questions.
    User will get a score shown at the end.
    if the user inputs a wrong character the question will be marked wrong.
    User is asked if they want to play another game.
    """

    print("Welcome to Maths Questions")
    choice_input = input(
        "Please choose" +
        "\n1 = Addition" +
        "\n2 = Subtraction" +
        "\n3 = Multiplication" +
        "\n4 = Exit Terminal \n")

    symbol = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }

    try:
        choice_input = int(choice_input)
        if choice_input == 1:
            symbol = "+"
            a = 1
            b = 5
            c = 1
            d = 5

        elif choice_input == 2:
            symbol = "-"
            a = 5
            b = 10
            c = 1
            d = 5

        elif choice_input == 3:
            symbol = "*"
            a = 1
            b = 5
            c = 1
            d = 5

        elif choice_input == 4:
            os.system('clear')
            exit_terminal()

        else:
            os.system('clear')
            random_maths_quiz()

    except ValueError:
        random_maths_quiz()

    os.system('clear')
    score = 0
    for i in range(5):
        num1 = random.randint(a, b)
        num2 = random.randint(c, d)

        expr = '{} {} {}'.format(num1, symbol, num2)
        result = eval(expr)
        guess_input = input(f"What is {num1} {symbol} {num2} =\n")

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
    sleep(3)
    os.system('clear')
    play_again()


def higher_lower():
    """
    Higher or Lower.
    The game begins by generating a random number between 1 and 50.
    The player's objective is to guess this randomly generated number.
    The game provides feedback on the guessed number.
    Higher, lower and the correct number.
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
    sleep(5)
    os.system('clear')
    play_again()


def number_facts():
    """
    Number Facts
    Gets the facts worksheet from google sheets.
    Once the values are got it randomly picks one fact from the list
    """

    facts = SHEET.worksheet('facts')
    facts = facts.get_all_values()
    facts_row = random.choice(facts)
    print(", ".join(facts_row))
    print("---------------------")
    while True:
        try:
            num_facts_input = input(
                "Would you like to another fact?\nY/N\n").lower()
            if num_facts_input == "y":
                os.system('clear')
                number_facts()

            elif num_facts_input == "n":
                os.system('clear')
                main()

        except ValueError:
            print("Please pick Y or N")


def play_again():
    """
    Play Again.
    After completing a quiz or game the user is asked
    do they want to play again.
    If yes the user is brought back to the main function to pick what to play.
    If no the terminal is closed.
    """

    play_again_input = input(
        "Would you like to play another game?\nY/N\n").lower()
    if play_again_input == "y":
        sleep(1)
        os.system('clear')
        main()

    elif play_again_input == "n":
        os.system('clear')
        exit_terminal()

    else:
        print("Please choose Y or N")
        play_again()


def exit_terminal():
    thanks = pyfiglet.figlet_format
    print(thanks("Thanks \nFor \nPlaying", font="big", justify="center"))
    sleep(5)
    os.system('clear')
    sys.exit(0)


def main():
    """
    Main Function
    This is the starting point for the execution of the program.
    Here the users have the choice to pick what they want to play.
    """
    os.system('clear')
    while True:
        try:
            header = pyfiglet.figlet_format
            print(header("NUMBERS\n", font="banner", justify="center"))
            choice_input = input(
                "Please choose \n1 = Simple Maths \n2 = Higher or Lower"
                "\n3 = Facts about Numbers \n4 = Exit Terminal\n")
            choice_input = int(choice_input)
            if choice_input == 1:
                os.system('clear')
                random_maths_quiz()

            elif choice_input == 2:
                os.system('clear')
                higher_lower()

            elif choice_input == 3:
                os.system('clear')
                number_facts()

            elif choice_input == 4:
                os.system('clear')
                exit_terminal()

            else:
                print("Something went wrong")
                sleep(1.5)
                os.system('clear')
                main()

        except ValueError:
            print("Please pick a number")
            sleep(2)


main()
