import argparse
import os
import random
import sys
from typing import Counter

ROOT_DIR = os.path.join(os.path.dirname(__file__), os.path.pardir)
MODULE_DIR = os.path.join(ROOT_DIR, "wordle_bot")
sys.path.insert(0, ROOT_DIR)

from wordle_bot.utils import colorize, load_word_list


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
    answer = random.choice(words)
    word_set = set(words)

    if args.debug:
        print(answer)

    loop_count = 100 if args.debug else 6

    for _ in range(loop_count):
        answer_set = Counter(answer)
        guess = None

        while guess not in word_set:
            guess = input("Guess> ").strip().lower()

        if guess == answer:
            print("YOU WIN!")
            break

        output = [None] * len(answer)

        def assign(prefix, ndx, letter):
            nonlocal output
            output[ndx] = prefix + letter
            answer_set[letter] -= 1

        for ndx, (letter, ans_letter) in enumerate(zip(guess, answer)):

            if letter == ans_letter:
                assign("+", ndx, letter)

        for ndx, (letter, ans_letter) in enumerate(zip(guess, answer)):

            if output[ndx] != None:
                continue

            if answer_set[letter] > 0:
                assign("~", ndx, letter)
            else:
                assign("-", ndx, letter)

        print(colorize(output))


if __name__ == "__main__":
    main()
