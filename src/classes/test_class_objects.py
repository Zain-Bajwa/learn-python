"""Class Definition Syntax.

@see: https://docs.python.org/3/tutorial/classes.html#class-objects

After defining the class attributes to a class, the class object can be created by assigning the
object to a variable. The created object would have instance attributes associated with it.
"""


def test_class_objects():
    """Class Objects.

    Class objects support two kinds of operations:
    - attribute references
    - instantiation.
    """

    # ATTRIBUTE REFERENCES use the standard syntax used for all attribute references in
    # Python: obj.name. Valid attribute names are all the names that were in the class’s namespace
    # when the class object was created. For class MyCounter the following references are valid
    # attribute references:

    class ComplexNumber:
        """Example of the complex numbers class"""

        real = 0
        imaginary = 0

        def get_real(self):
            """Return real part of complex number."""
            return self.real

        def get_imaginary(self):
            """Return imaginary part of complex number."""
            return self.imaginary

    assert ComplexNumber.real == 0

    # __doc__ is also a valid attribute, returning the docstring belonging to the class
    assert ComplexNumber.__doc__ == 'Example of the complex numbers class'

    # Class attributes can also be assigned to, so you can change the value of
    # ComplexNumber.counter by assignment.
    ComplexNumber.real = 10
    assert ComplexNumber.real == 10

    # CLASS INSTANTIATION uses function notation. Just pretend that the class object is a
    # parameterless function that returns a new instance of the class. For example
    # (assuming the above class):
    complex_number = ComplexNumber()

    complex_number_2 = ComplexNumber()

    assert complex_number.real == 10
    assert complex_number.get_real() == 10

    assert complex_number_2.real == 10
    assert complex_number_2.get_real() == 10

    # Change the value of real for instance complex_number
    complex_number.real = 20
    ComplexNumber.real = 30

    assert complex_number.real == 20
    assert complex_number.get_real() == 20

    assert complex_number_2.real == 30
    assert complex_number_2.get_real() == 30

    # Let's change counter default value back.
    ComplexNumber.real = 10
    assert ComplexNumber.real == 10

    # The instantiation operation (“calling” a class object) creates an empty object. Many classes
    # like to create objects with instances customized to a specific initial state. Therefore a
    # class may define a special method named __init__(), like this:

    class ComplexNumberWithConstructor:
        """Example of the class with constructor"""
        def __init__(self, real_part, imaginary_part):
            self.real = real_part
            self.imaginary = imaginary_part

        def get_real(self):
            """Return real part of complex number."""
            return self.real

        def get_imaginary(self):
            """Return imaginary part of complex number."""
            return self.imaginary
    
    class ComplexNumberWithDefaultConstructor:
        """Example of the class with default and parameterized constructor"""
        def __init__(self, real_part = 0, imaginary_part = 0):
            """parameterized constructor"""
            
            self.real = real_part
            self.imaginary = imaginary_part

        def set_real(self, real):
            """Set real part of complex number"""
            self.real = real

        def set_imaginary(self, imaginary):
            """Set imaginary part of complex number"""
            self.imaginary = imaginary

        def get_real(self):
            """Return real part of complex number."""
            return self.real

        def get_imaginary(self):
            """Return imaginary part of complex number."""
            return self.imaginary

    complex_number = ComplexNumberWithConstructor(3.0, -4.5)
    assert complex_number.real, complex_number.imaginary == (3.0, -4.5)

    complex_number_2 = ComplexNumberWithDefaultConstructor()
    complex_number_2.set_real(10)
    complex_number_2.set_imaginary(4)
    assert complex_number_2.get_real(), complex_number_2.get_imaginary() == (10, 4)


test_class_objects()
