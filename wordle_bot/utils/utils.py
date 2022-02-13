import json
from typing import Counter

import colored


def load_word_list():
    words = json.load(open("word_list.json"))
    return words


def colorize(guess_response):
    COLOR_MAP = {
        "+": "light_green",
        "~": "light_yellow",
        "-": "dark_gray",
    }
    colorized = ""
    for prefix, letter in guess_response:
        colorized += colored.stylize(letter, (colored.fg(COLOR_MAP[prefix])))
    return colorized


def check_guess(guess, answer):
    output = [None] * len(answer)
    answer_set = Counter(answer)

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
    return output
