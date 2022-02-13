import argparse
import os
import random
import sys

ROOT_DIR = os.path.join(os.path.dirname(__file__), os.path.pardir)
MODULE_DIR = os.path.join(ROOT_DIR, "wordle_bot")
sys.path.insert(0, ROOT_DIR)

from wordle_bot.utils import colorize, load_word_list, check_guess


def main():
    parser = argparse.ArgumentParser(description="Wordle Game")
    parser.add_argument(
        "-d",
        "--debug",
        help="Runs wordle in debug mode enabling 100 guesses and shows the answer",
        action="store_true",
        default=False,
    )

    args, _ = parser.parse_known_args()

    words = load_word_list()
    word_set = set(words)

    answer = random.choice(words)

    if args.debug:
        print(answer)

    loop_count = 100 if args.debug else 6

    for _ in range(loop_count):
        guess = None

        while guess not in word_set:
            guess = input("Guess> ").strip().lower()

        if guess == answer:
            print("YOU WIN!")
            break
        printed_guess = check_guess(guess, answer)
        if args.debug:
            print("".join(printed_guess))
        print(colorize(printed_guess))


if __name__ == "__main__":
    main()
