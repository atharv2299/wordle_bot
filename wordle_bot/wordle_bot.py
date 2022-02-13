from typing import Counter


def score_words(word_list, counter_list):

    for word in word_list:
        for ndx, letter in enumerate(word):
            counter_list[ndx][letter] += 1

    max_score = 0
    best_word = None
    for word in word_list:
        current_score = 0
        seen_letter = Counter(word)
        for ndx, letter in enumerate(word):
            current_score += counter_list[ndx][letter] / seen_letter[letter]

        if current_score > max_score:
            max_score = current_score
            best_word = word
    return best_word


def keep_word(prefix, letter, guess_letter, has_letter):
    if prefix == "+" and letter != guess_letter:
        return False
    if prefix == "~" and (not has_letter or letter == guess_letter):
        return False
    if prefix == "-" and has_letter:
        return False
    return True


def keep_guess(prefix, letter, guess_letter, has_letter):
    if prefix in ["+", "~"] and letter == guess_letter:
        return False
    if prefix == "-" and has_letter:
        return False
    return True


def prune_list(word_list, annotated_guess, func):
    def matches(word):
        for letter, (prefix, guess_letter) in zip(word, annotated_guess):
            has_letter = guess_letter in word
            if not func(prefix, letter, guess_letter, has_letter):
                return False
        return True

    return filter(matches, word_list)
