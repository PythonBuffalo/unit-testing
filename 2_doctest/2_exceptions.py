def remove_newline(text):
    """Remove all new line characters from provided text

    >>> remove_newline('hello\\nworld')
    'helloworld'
    >>> remove_newline(5)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 2, in remove_newline
    AttributeError: 'int' object has no attribute 'replace'
    """
    return text.replace('\n', '')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
