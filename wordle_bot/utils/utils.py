import json

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
