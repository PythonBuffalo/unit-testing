class TestClass(object):
    """TestClass holds a unique set of numbers

    >>> tc = TestClass([4, 5, 6, 6, 6, 6, 6])
    >>> tc.add_number(2)
    >>> tc.add_numbers([5, 6, 7])
    >>> tc.add_number(3)
    >>> tc.numbers
    set([2, 3, 4, 5, 6, 7])
    """

    def __init__(self, numbers):
        """Constructor for TestClass

        >>> tc = TestClass([3, 4, 5, 5])
        >>> tc.numbers
        set([3, 4, 5])
        """
        self.numbers = set(numbers)

    def add_number(self, number):
        """Add a new number to TestClass.numbers

        >>> tc = TestClass([])
        >>> tc.add_number(5)
        >>> tc.numbers
        set([5])
        >>> tc.add_number(5)
        >>> tc.numbers
        set([5])
        """
        self.numbers.add(number)

    def add_numbers(self, numbers):
        """Add multiple numbers to TestClass.numbers

        >>> tc = TestClass([4, 5, 6, 6])
        >>> tc.add_numbers([4, 5, 6, 7])
        >>> tc.numbers
        set([4, 5, 6, 7])
        """
        self.numbers |= set(numbers)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
