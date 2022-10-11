def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    lower = to_swap.lower()
    upper = to_swap.upper()

    result = ''

    for char in phrase:
        if char == lower:
            result += upper
        elif char == upper:
            result += lower
        else:
            result += char

    return result
        
