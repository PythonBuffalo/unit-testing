def factorial(num):
    """A function to compute the factorial of a provided number

    >>> factorial(5)
    120
    >>> factorial(25)
    15511210043330985984000000L
    >>> factorial(-5)
    1
    """
    if num <= 0:
        return 1
    else:
        return num * factorial(num - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
