"""Dictionaries.

@see: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
@see: https://www.w3schools.com/python/python_dictionaries.asp

A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are
written with curly brackets, and they have keys and values.

Dictionaries are sometimes found in other languages as “associative memories” or “associative
arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by
keys, which can be any immutable type; strings and numbers can always be keys. Tuples can be used
as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object
either directly or indirectly, it cannot be used as a key. You can’t use lists as keys, since
lists can be modified in place using index assignments, slice assignments, or methods like append()
and extend().

It is best to think of a dictionary as a set of key: value pairs, with the requirement that the
keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}.
Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs
to the dictionary; this is also the way dictionaries are written on output.
"""


def test_dic_comprehension():
    # map list into dictionary as square of numbers
    numbers = [1, 2, 3, 4, 5, 6]
    square_dict = dict()
    for i in numbers:
        square_dict[i] = i ** 2
    print(square_dict)
    # now with dict compression
    new_dict = {i: i ** 2 for i in numbers}
    print(new_dict)


def test_dic_comprehension1():
    # Lets we have a dictionary of items with price
    old_price = {"milk": 1.5, "coffee": 2.05, "bread": 3.0}

    # Increase 50% price if the price is greater than 2 other vise price will be same
    new_price = {key: value * 1.5 if value > 2.0 else value for key, value in old_price.items()}
    print(new_price)


def test_dic_function():
    dic = {'a': 4098, 'd': 4139}
    dic['c'] = 4050
    assert dic == {'a': 4098, 'd': 4139, 'c': 4050}

    del dic['d']
    dic['b'] = 4127
    assert dic == {'a': 4098, 'b': 4127, 'c': 4050}
    assert list(dic) == ['a', 'c', 'b']
    assert sorted(dic) == ['a', 'b', 'c']
    assert list(dic.values()) == [4098, 4050, 4127]
    assert sorted(dic.values()) == [4050, 4098, 4127]
    assert 'a' in dic
    assert 'Ali' not in dic


def test_dictionary():
    """Dictionary"""

    fruits_dictionary = {
        'cherry': 'red',
        'apple': 'green',
        'banana': 'yellow',
    }

    assert isinstance(fruits_dictionary, dict)

    # You may access set elements by keys.
    assert fruits_dictionary['apple'] == 'green'
    assert fruits_dictionary['banana'] == 'yellow'
    assert fruits_dictionary['cherry'] == 'red'

    # To check whether a single key is in the dictionary, use the in keyword.
    assert 'apple' in fruits_dictionary
    assert 'pineapple' not in fruits_dictionary

    # Change the apple color to "red".
    fruits_dictionary['apple'] = 'red'

    # Add new key/value pair to the dictionary
    fruits_dictionary['pineapple'] = 'yellow'
    assert fruits_dictionary['pineapple'] == 'yellow'

    # Performing list(d) on a dictionary returns a list of all the keys used in the dictionary,
    # in insertion order (if you want it sorted, just use sorted(d) instead).
    assert list(fruits_dictionary) == ['cherry', 'apple', 'banana', 'pineapple']
    assert sorted(fruits_dictionary) == ['apple', 'banana', 'cherry', 'pineapple']

    # It is also possible to delete a key:value pair with del.
    del fruits_dictionary['pineapple']
    assert list(fruits_dictionary) == ['cherry', 'apple', 'banana']

    # The dict() constructor builds dictionaries directly from sequences of key-value pairs.
    dictionary_via_constructor = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

    assert dictionary_via_constructor['sape'] == 4139
    assert dictionary_via_constructor['guido'] == 4127
    assert dictionary_via_constructor['jack'] == 4098

    # In addition, dict comprehensions can be used to create dictionaries from arbitrary key
    # and value expressions:
    dictionary_via_expression = {x: x**2 for x in (2, 4, 6)}
    assert dictionary_via_expression[2] == 4
    assert dictionary_via_expression[4] == 16
    assert dictionary_via_expression[6] == 36

    # When the keys are simple strings, it is sometimes easier to specify pairs using
    # keyword arguments.
    dictionary_for_string_keys = dict(sape=4139, guido=4127, jack=4098)
    assert dictionary_for_string_keys['sape'] == 4139
    assert dictionary_for_string_keys['guido'] == 4127
    assert dictionary_for_string_keys['jack'] == 4098


test_dic_comprehension()

test_dic_comprehension1()

test_dic_function()
