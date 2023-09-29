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
        playAgain()


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

def higher_lower():


def play_again():


def main():


main():