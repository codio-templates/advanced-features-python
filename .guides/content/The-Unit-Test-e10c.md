# Sample content New Page

You can upload any unit tests you already have to Codio. Scripts should be kept in the `.guides` folder so that students do not have access to them.

## The Setup
[See the Setup](open_file .guides/test_circle_area.py panel=0 ref="import" count=5)

Import the `unittest` module, the `circle_area` function from the student code, and `pi` from the `math` module. The test should be a subclass of `TestCase`. 

## Test the Output
[See the Output Test](open_file .guides/test_circle_area.py panel=0 ref="def test_area" count=4)

Create several cases that test the end result of the student. Testing parameters like 0 and 1 are simple to do, but be sure to other numbers to verify the function is working as expected.

## Test Parameter Values
[See the Value Test](open_file .guides/test_circle_area.py panel=0 ref="def test_values" count=2)

Circles cannot have a negative radius, so the student code should raise a value error when a negative number is passed to the function.

## Test Parameter Types
[See the Type Test](open_file .guides/test_circle_area.py panel=0 ref="def test_types" count=4)

A circle's radius cannot be expressed as a string or boolean value. In addition, a radius must be a real number. In Python, `j` represents the square root of -1. Verify that the student code raises a type error when parameters are not a real number.

