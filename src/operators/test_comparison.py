"""Comparison operators

@see: https://www.w3schools.com/python/python_operators.asp

Comparison operators are used to compare two values.
"""


def test_comparison_operators():
    """Comparison operators"""

    # Equal.
    number = 5
    assert number == 5
    assert number == 5.0

    # Not equal.
    number = 5
    assert number != 3
    assert number != 3.000000000000001

    # Greater than.
    number = 5
    assert number > 3

    # Less than.
    number = 5
    assert number < 8

    # Greater than or equal to
    number = 5
    assert number >= 5
    assert number >= 4

    number = 5.00000000000001
    assert number >= 5
    assert number >= 4

    # Less than or equal to
    number = 5
    assert number <= 5
    assert number <= 6


test_comparison_operators()
