from typing import Counter


def score_words(word_list, counter_list):

    for word in word_list:
        for ndx, letter in enumerate(word):
            counter_list[ndx][letter] += 1

    score_dict = {}
    for word in word_list:
        current_score = 0
        seen_letter = Counter(word)

        for ndx, letter in enumerate(word):
            current_score += counter_list[ndx][letter] / seen_letter[letter]

        if current_score not in score_dict:
            score_dict[current_score] = []
        score_dict[current_score].append(word)

    return score_dict[sorted(score_dict)[-1]]


def keep_word(prefix, letter, guess_letter, has_letter, allowed_counts):
    if prefix == "+" and letter != guess_letter:
        return False
    if prefix == "~" and (not has_letter or letter == guess_letter):
        return False
    if prefix == "-" and has_letter and allowed_counts[guess_letter] <= 0:
        return False
    return True


def keep_guess(prefix, letter, guess_letter, has_letter, allowed_counts):
    if prefix in ["+", "~"] and letter == guess_letter:
        return False
    if prefix == "-" and has_letter and allowed_counts[guess_letter] <= 0:
        return False
    return True


def prune_list(word_list, annotated_guess, func):
    def matches(word):
        allowed_counts = Counter()
        for prefix, guess_letter in annotated_guess:
            if prefix in ["~", "+"]:
                allowed_counts[guess_letter] += 1

        for letter, (prefix, guess_letter) in zip(word, annotated_guess):
            has_letter = guess_letter in word
            if not func(prefix, letter, guess_letter, has_letter, allowed_counts):
                return False
            allowed_counts[letter] -= 1
        return True

    return filter(matches, word_list)
