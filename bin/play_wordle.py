import os
import sys

from typing import Counter

ROOT_DIR = os.path.join(os.path.dirname(__file__), os.path.pardir)
MODULE_DIR = os.path.join(ROOT_DIR, "wordle_bot")
sys.path.insert(0, ROOT_DIR)

from wordle_bot.utils import check_guess, colorize, load_word_list, chunks
from wordle_bot import score_words, prune_list


def main():
    word_list = load_word_list()
    WORD_LEN = len(word_list[0])
    pruned_list = word_list

    while True:
        counter_list = [Counter()] * WORD_LEN
        best_guess = score_words(pruned_list, counter_list)
        print(best_guess)
        annotated_guess = input("Annotated Guess> ").strip().lower()
        pruned_list = list(prune_list(pruned_list, list(chunks(annotated_guess))))
        # print(pruned_list[:20])


if __name__ == "__main__":
    main()
