import json


def load_word_list():
    words = json.load(open("word_list.json"))
    return words


def colorize(guess_response):
    # output[ndx] = colored.stylize(letter, colored.fg(color))

    return guess_response
