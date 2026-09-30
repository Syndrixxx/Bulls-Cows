import string
import random

SEPARATOR = "-" * 45

def random_number() -> int:
    """Generates a random four-digit number with unique digits.

    :return: A random four-digit number.
    :rtype: int
    """
    first_number = random.choice("123456789")
    rest_of_numbers = random.sample(string.digits.replace(first_number, ""), k=3)

    return int(first_number + "".join(rest_of_numbers))

def bulls_count(num1: str | int, num2: str | int) -> int:
    """Counts the digits that match in both value and position.

    :param num1: The secret number.
    :type num1: str | int
    :param num2: The guessed number.
    :type num2: str | int
    :return: The number of bulls.
    :rtype: int
    """
    count = 0

    for secret_number, guessed_number in zip(str(num1), str(num2)):
        if secret_number == guessed_number:
            count += 1

    return count

def cows_count(num1: str | int, num2: str | int) -> int:
    """Counts the digits that are present in both numbers.

    :param num1: The secret number.
    :type num1: str | int
    :param num2: The guessed number.
    :type num2: str | int
    :return: The number of common digits.
    :rtype: int
    """
    common_digits = set(str(num1)) & set(str(num2))
    
    return len(common_digits)

def plural_or_singular(word:str, amount:int) -> str:
    """Returns the word in singular or plural form based on the amount.

    :param word: The word to convert to singular or plural form.
    :type word: str
    :param amount: The amount used to determine the grammatical form.
    :type amount: int
    :return: The word in singular or plural form.
    :rtype: str
    """
    if amount == 1:
        return word

    return f"{word}s"

def main():
    """Runs the main game loop and controls the game flow."""

    print("Hi there!")
    print(SEPARATOR)
    print("""I've generated a random 4 digit number for you.
    Let's play a bulls and cows game.""")
    print(SEPARATOR)

    correct_number = random_number()
    number_of_tries = 0

    while True:
        chosen_number = input("Enter a number:")
        if len(chosen_number) != 4:
            print("Number is not the right length, should be 4 numbers.")
            print("Try again!")
            print(SEPARATOR)
            continue

        elif not chosen_number.isnumeric():
            print("Input should contain only numbers!")
            print("Try again!")
            print(SEPARATOR)
            continue

        elif chosen_number.startswith("0"):
            print("Entered number cannot start with a 0 (must be 1-9)")
            print("Try again!")
            print(SEPARATOR)
            continue

        elif len(set(chosen_number)) != 4:
            print("There are not allowed duplicate numbers, each one must be unique!")
            print("Try again!")
            print(SEPARATOR)
            continue

        else:
            number_of_tries += 1

            if correct_number != int(chosen_number):
                bulls = bulls_count(correct_number, chosen_number)
                cows = cows_count(correct_number, chosen_number) - bulls
                out_bulls = f"{bulls} {plural_or_singular('Bull', bulls)}"
                out_cows = f"{cows} {plural_or_singular('Cow', cows )}"
                print(SEPARATOR)
                print(f">>> {chosen_number}")
                print(", ".join((out_bulls, out_cows)))
                print(SEPARATOR)
                continue

            else:
                print(SEPARATOR)
                print(f">>> {chosen_number}")
                print(f"Correct, you've guessed the right number in {number_of_tries} guesses!")
                print(SEPARATOR)
                print("That's amazing!")
                break

if __name__ == "__main__":
    main()