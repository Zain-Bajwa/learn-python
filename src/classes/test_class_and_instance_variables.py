"""Class and Instance Variables.

@see: https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables

Generally speaking, instance variables are for data unique to each instance and class variables are
for attributes and methods shared by all instances of the class.
"""


def test_class_and_instance_variables():
    """Class and Instance Variables."""

    # pylint: disable=too-few-public-methods
    class Dog:
        """Dog class example"""
        kind = 'canine'  # Class variable shared by all instances.

        def __init__(self, name):
            self.name = name  # Instance variable unique to each instance.

    fido = Dog('Fido')
    buddy = Dog('Buddy')

    # Shared by all dogs.
    assert fido.kind == 'canine'
    assert buddy.kind == 'canine'

    # Unique to fido.
    assert fido.name == 'Fido'

    # Unique to buddy.
    assert buddy.name == 'Buddy'

    # Change value of kind variable
    fido.kind = "husky"

    assert fido.kind == "husky"
    assert fido.kind == "husky"

    # Shared data can have possibly surprising effects with involving mutable objects such as lists
    # and dictionaries. For example, the tricks list in the following code should not be used as a
    # class variable because just a single list would be shared by all Dog instances.

    # pylint: disable=too-few-public-methods
    class DogWithSharedTricks:
        """Dog class example with wrong shared variable usage"""
        tricks = []  # Mistaken use of a class variable (see below) for mutable objects.

        def __init__(self, name):
            self.name = name  # Instance variable unique to each instance.

        def add_trick(self, trick):
            """Add trick to the dog

            This function illustrate mistaken use of mutable class variable tricks (see below).
            """
            self.tricks.append(trick)

    fido = DogWithSharedTricks('Fido')
    buddy = DogWithSharedTricks('Buddy')

    fido.add_trick('roll over')
    buddy.add_trick('play dead')

    assert fido.tricks == ['roll over', 'play dead']  # unexpectedly shared by all dogs
    assert buddy.tricks == ['roll over', 'play dead']  # unexpectedly shared by all dogs

    # Correct design of the class should use an instance variable instead:

    # pylint: disable=too-few-public-methods
    class DogWithTricks:
        """Dog class example"""

        def __init__(self, name):
            self.name = name  # Instance variable unique to each instance.
            self.tricks = []  # creates a new empty list for each dog

        def add_trick(self, trick):
            """Add trick to the dog

            This function illustrate a correct use of mutable class variable tricks (see below).
            """
            self.tricks.append(trick)

    fido = DogWithTricks('Fido')
    buddy = DogWithTricks('Buddy')

    fido.add_trick('roll over')
    buddy.add_trick('play dead')

    assert fido.tricks == ['roll over']
    assert buddy.tricks == ['play dead']

    buddy.add_trick("spin")
    assert buddy.tricks == ['play dead', 'spin']

    class Day:
        """Day class for storing daily records"""

        def __init__(self, day, min_temperature, max_temperature):
            self.day = day
            self.min_temperature = min_temperature
            self.max_temperature = max_temperature
        
        def __str__(self):
            """Print Data member

            Print values of min_temperature and max_temperature
            """
            return f"Day: {self.day}\tMin: {self.min_temperature}\tMax: {self.max_temperature}"

    class Month:
        """Month class of holding a list of all days in a month"""

        def __init__(self, month):
            self.month = month
            self.days = []
        
        def add_day_in_month(self, month, day):
            """Add a day

            Add a record of a day in a specific month
            """
            if self.month == month:
                self.days.append(day)
        
        def display_all_days(self, month):
            """Print all days of a month"""
            if self.month == month:
                for day in self.days:
                    print(f"Month: {self.month}\t{day}")

    
    # Add data of few days for month Junuary
    d1 = Day(1, 4, 23)
    d2 = Day(2, 5, 22)
    d3 = Day(3, 3, 24)
    d4 = Day(4, 4, 22)

    # Add list of days in a month Junuary
    junuary = Month("Junuary")
    junuary.add_day_in_month("Junuary", d1)
    junuary.add_day_in_month("Junuary", d2)
    junuary.add_day_in_month("Junuary", d3)
    junuary.add_day_in_month("Junuary", d4)

    # Display all days of Junuary
    junuary.display_all_days("Junuary")

    # Add data of few days for month February
    d1 = Day(3, 4, 16)
    d2 = Day(5, 4, 20)
    d3 = Day(6, 0, 24)
    d4 = Day(7, -3, 17)

    # Add list of days in a month Junuary
    junuary = Month("February")
    junuary.add_day_in_month("February", d1)
    junuary.add_day_in_month("February", d2)
    junuary.add_day_in_month("February", d3)
    junuary.add_day_in_month("February", d4)

    # Display all days of Junuary
    junuary.display_all_days("February")


test_class_and_instance_variables()
