def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    total = {}
    # val = 1
    # for letter in phrase:
    #     total.get(letter, val)
    # else:
    #     total.update({letter, })
    # return total
    for letter in phrase:
        if letter not in total:
            total[letter] = 1
        else:
            total[letter] = total[letter] + 1
    return total


