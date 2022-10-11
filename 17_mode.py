def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    freq = {}
    max_val = 0
    most_common_number = None

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    for (key, value) in freq.items():
        if value > max_val:
            most_common_number = key
            max_val = value

    return most_common_number
