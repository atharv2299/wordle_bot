from typing import Counter
import math


def score_words(word_list, guess_list):
    WORD_LEN = len(word_list[0])
    counter_list = [Counter() for _ in range(WORD_LEN)]

    for word in word_list:
        for ndx, letter in enumerate(word):
            counter_list[ndx][letter] += 1

    for counter in counter_list:
        counter_sum = sum(counter.values())
        for letter in counter:
            probability = counter[letter] / counter_sum + 0.2
            counter[letter] = probability * -math.log(probability, 2)

    collapsed_entropy = Counter()
    for counter in counter_list:
        collapsed_entropy.update(counter)

    max_score = -math.inf
    best_word = None

    for word in guess_list:
        current_score = 0
        seen_letter = Counter(word)

        for ndx, letter in enumerate(word):
            current_score += collapsed_entropy[letter] / seen_letter[letter]

        if current_score > max_score:
            max_score = current_score
            best_word = word
    return best_word


def keep_word(word, annotated_guess):

    allowed_counts = Counter()

    for prefix, guess_letter in annotated_guess:

        if prefix in ["~", "+"]:
            allowed_counts[guess_letter] += 1

    word_counter = Counter(word)

    for prefix, guess_letter in annotated_guess:

        if prefix == "-":

            if word_counter[guess_letter] > allowed_counts[guess_letter]:
                return False

    for letter, (prefix, guess_letter) in zip(word, annotated_guess):

        if prefix == "+" and letter != guess_letter:
            return False

        if prefix == "~" and (not guess_letter in word or letter == guess_letter):
            return False
    return True


def keep_guess(word, annotated_guess):
    # allowed_counts = Counter()

    # for prefix, guess_letter in annotated_guess:

    #     if prefix in ["~", "+"]:
    #         allowed_counts[guess_letter] += 1

    # word_counter = Counter(word)

    # for prefix, guess_letter in annotated_guess:

    #     if prefix == "-":

    #         if word_counter[guess_letter] > allowed_counts[guess_letter]:
    #             return False

    for letter, (prefix, guess_letter) in zip(word, annotated_guess):
        if prefix == "-" and guess_letter in word:
            return False
    return True


def prune_list(word_list, annotated_guess, func):
    def matches(word):
        return func(word, annotated_guess)

    return filter(matches, word_list)
