def remove_twos(numbers):
    """Function to remove all 2's from a list

    >>> numbers = [3, 4, 8, 2, 4, 2, 3, 5, 2]
    >>> results = remove_twos(numbers)
    >>> type(results)
    <type 'generator'>
    >>> list(results)
    [3, 4, 8, 4, 3, 5]
    """
    for num in numbers:
        if num != 2:
            yield num


if __name__ == '__main__':
    import doctest
    doctest.testmod()
