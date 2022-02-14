import os
import sys
import colored
from typing import Counter

ROOT_DIR = os.path.join(os.path.dirname(__file__), os.path.pardir)
MODULE_DIR = os.path.join(ROOT_DIR, "wordle_bot")
sys.path.insert(0, ROOT_DIR)

from wordle_bot.utils import check_guess, colorize, load_word_list, chunks
from wordle_bot import score_words, prune_list, keep_word, keep_guess


def main():
    word_list = load_word_list()
    pruned_list = word_list
    guess_list = word_list
    while len(pruned_list) > 1:

        # TODO: ENDGAME PLAYING
        # check_set = set("".join(pruned_list))
        # # 5 is the base number of letters in the set, so you want to see if you have one different letter per list element
        # if len(check_set) < len(pruned_list) + 5:
        #     print(None)

        best_guess = score_words(guess_list if len(guess_list) > 0 else pruned_list)
        print(colored.stylize(best_guess, (colored.fg("light_green"))))

        annotated_guess = list(chunks(input("Annotated Guess> ").strip().lower()))

        pruned_list = list(prune_list(pruned_list, annotated_guess, keep_word))
        print(pruned_list)

        guess_list = list(prune_list(guess_list, annotated_guess, keep_guess))

    print(pruned_list[0])


if __name__ == "__main__":
    main()
