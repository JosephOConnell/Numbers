import random


def random_maths_quiz():
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
    print("to be added")


def play_again():
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
    random_maths_quiz()


main()
