"""Membership operators

@see: https://www.w3schools.com/python/python_operators.asp

Membership operators are used to test if a sequence is presented in an object.
"""


def test_membership_operators():
    """Membership operators"""

    # Let's use the following fruit list to illustrate membership concept.
    fruit_list = ["apple", "banana"]
    


    # in
    # Returns True if a sequence with the specified value is present in the object.

    # Returns True because a sequence with the value "banana" is in the list
    assert "banana" in fruit_list

    # not in
    # Returns True if a sequence with the specified value is not present in the object

    # Returns True because a sequence with the value "pineapple" is not in the list.
    assert "pineapple" not in fruit_list

    # Member of a tuple
    number_tuple = (1, 3, 4, 5, 10)
    assert 5 in number_tuple

    # member of a string
    message = "Hello World"
    assert 'Hello' in message
    assert ' ' in message


test_membership_operators()
