import os
import sys
import colored
from typing import Counter
import argparse

ROOT_DIR = os.path.join(os.path.dirname(__file__), os.path.pardir)
MODULE_DIR = os.path.join(ROOT_DIR, "wordle_bot")
sys.path.insert(0, ROOT_DIR)

from wordle_bot.utils import check_guess, colorize, load_word_list, chunks, colorify
from wordle_bot import score_words, prune_list, keep_word, keep_guess


def main():
    parser = argparse.ArgumentParser(description="Wordle Game")
    parser.add_argument(
        "-d",
        "--debug",
        help="Runs wordle bot in debug mode prints the pruned list and guessing list",
        action="store_true",
        default=False,
    )

    args, _ = parser.parse_known_args()

    word_list = load_word_list()
    pruned_list = word_list
    guess_list = word_list

    while len(pruned_list) > 1:

        # TODO: ENDGAME PLAYING
        # check_set = set("".join(pruned_list))
        # # 5 is the base number of letters in the set, so you want to see if you have one different letter per list element
        # if len(check_set) < len(pruned_list) + 5:
        #     print(None)

        best_guess = score_words(pruned_list, word_list)

        print(colorify("=" * 20, "light_green"))
        print("I suggest: " + colorify(best_guess, "light_green"))
        print(colorify("=" * 20, "light_green"))

        annotated_guess = list(chunks(input("Annotated Guess> ").strip().lower()))

        pruned_list = list(prune_list(pruned_list, annotated_guess, keep_word))
        guess_list = list(prune_list(guess_list, annotated_guess, keep_guess))

        if args.debug:
            print(pruned_list)
            print("=" * 20)
            print(guess_list)

    print(colorify("=" * 20, "light_green"))
    print(colorify(pruned_list[0], "light_green"))
    print(colorify("=" * 20, "light_green"))


if __name__ == "__main__":
    main()
