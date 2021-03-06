

from itertools import islice, chain


def grouper(iterable, size):

    """
    Yield "groups" from an iterable.

    Args:
        iterable (iter): The iterable.
        size (int): The number of elements in each group.

    Yields:
        The next group.
    """

    source = iter(iterable)

    while True:
        group = islice(source, size)
        yield chain([next(group)], group)


def enum(*seq, **named):

    """
    Make an enumerated type.

    Returns: type
    """

    enums = dict(zip(seq, range(len(seq))), **named)

    return type('Enum', (), enums)
