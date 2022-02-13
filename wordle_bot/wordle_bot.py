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
