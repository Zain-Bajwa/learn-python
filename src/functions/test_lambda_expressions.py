"""Lambda Expressions

@see: https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions

Small anonymous functions can be created with the lambda keyword. Lambda functions can be used
wherever function objects are required. They are syntactically restricted to a single expression.
Semantically, they are just syntactic sugar for a normal function definition. Like nested function
definitions, lambda functions can reference variables from the containing scope.
"""


def test_lambda_expressions():
    """Lambda Expressions"""

    # This function returns the sum of its two arguments: lambda a, b: a+b
    # Like nested function definitions, lambda functions can reference variables from the
    # containing scope.

    def make_increment_function(delta):
        """This example uses a lambda expression to return a function"""
        return lambda number: number + delta

    increment_function = make_increment_function(42)

    assert increment_function(0) == 42
    assert increment_function(1) == 43
    assert increment_function(2) == 44

    # Another use of lambda is to pass a small function as an argument.
    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    # Sort pairs by text key.
    pairs.sort(key=lambda pair: pair[1])

    assert pairs == [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]


def test_myfunc(n):

    # Say you have a function definition that takes one argument, and that argument will be
    # multiplied with an unknown number:
    return lambda a: a * n


def test_lambda_with_map():

    # Program to filter out only the even items from a list
    my_list = [1, 5, 4, 6, 8, 11, 3, 12]

    new_list = list(filter(lambda x: (x % 2 == 0), my_list))
    assert new_list == [4, 6, 8, 12]


def test_lambda_with_filter():
    # Program to double each item in a list using map()

    my_list = [1, 5, 4, 6, 8, 11, 3, 12]

    new_list = list(map(lambda x: x * 2, my_list))

    assert new_list == [2, 10, 8, 12, 16, 22, 6, 24]


test_lambda_expressions()
my_doubler = test_myfunc(2)
my_tripler = test_myfunc(3)

assert my_doubler(11) == 22
assert my_doubler(15) == 30

assert my_tripler(10) == 30

test_lambda_with_map()
test_lambda_with_filter()
