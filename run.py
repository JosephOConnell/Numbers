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


    def addition_and_subtraction():


def higher_lower():


def play_again():


def main():


main():