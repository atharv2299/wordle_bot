import os
import sys

from typing import Counter

ROOT_DIR = os.path.join(os.path.dirname(__file__), os.path.pardir)
MODULE_DIR = os.path.join(ROOT_DIR, "wordle_bot")
sys.path.insert(0, ROOT_DIR)

from wordle_bot.utils import check_guess, colorize, load_word_list
from wordle_bot import score_words


def main():
    word_list = load_word_list()
    WORD_LEN = len(word_list[0])
    counter_list = [Counter()] * WORD_LEN

    best_guess = score_words(word_list, counter_list)


if __name__ == "__main__":
    main()
