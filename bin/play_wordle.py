import argparse
import os
import sys
import random

ROOT_DIR = os.path.join(os.path.dirname(__file__), os.path.pardir)
MODULE_DIR = os.path.join(ROOT_DIR, "wordle_bot")
sys.path.insert(0, ROOT_DIR)

from wordle_bot import prune_list, score_words
from wordle_bot.utils import check_guess, chunks, colorify, load_word_list


def main():
    parser = argparse.ArgumentParser(description="Wordle Game")
    parser.add_argument(
        "-d",
        "--debug",
        help="Runs wordle bot in debug mode prints the pruned list and guessing list",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-a",
        "--autoplay",
        help="Set target word to automatically play through",
        nargs="?",
        action="append",
        default=None,
    )

    args, _ = parser.parse_known_args()

    word_list = load_word_list()
    pruned_list = word_list
    num_steps = 0
    guesses = []
    if args.autoplay is not None:
        autoplay = args.autoplay[0] or random.choice(word_list)
        print(autoplay)

    while len(pruned_list) > 1:
        num_steps += 1

        best_guess = score_words(pruned_list, word_list)
        word_list.remove(best_guess)
        guesses.append(best_guess)

        print(colorify("=" * 20, "light_green"))
        print(colorify(best_guess, "light_green"))
        print(colorify("=" * 20, "light_green"))

        if args.autoplay is None:
            annotated_guess = list(chunks(input("Annotated Guess> ").strip().lower()))
        else:
            annotated_guess = check_guess(best_guess, autoplay)

        pruned_list = list(prune_list(pruned_list, annotated_guess))

        if args.debug:
            print(pruned_list)
            print("=" * 20)

    print(colorify("=" * 20, "light_green"))
    print(colorify(pruned_list[0], "light_green"))
    print(colorify("=" * 20, "light_green"))
    if args.debug:
        print(colorify(", ".join(guesses), "light_blue"))
    print(f"Won in {num_steps} steps!")


if __name__ == "__main__":
    main()
