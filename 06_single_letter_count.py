def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """

    lower_case_word = word.lower()
    lower_case_letter = letter.lower()

    return lower_case_word.count(lower_case_letter)

    # return len([ltr for ltr in lower_case_word if ltr == lower_case_letter])

    # count = 0
    # for ltr in lower_case_word:
    #     if ltr == lower_case_letter:
    #         count += 1

    # return count
