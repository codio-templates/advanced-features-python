# Sample content New Page

You can upload any unit tests you already have to Codio. Scripts should be kept in the `.guides/secure` folder so that students do not have access to them. **Note**, this example assumes a straight points problem (no partial points), so points are assigned to the student only if all of the tests pass. A partial points example in in the next section.

## The Setup
[See the Setup](open_file .guides/secure/test_circle_area.py panel=0 ref="import" count=5)

Since the test file is in `.guides/secure` and the student file is another directory, we need to append the system path so that the unit test can "see" the student work. Be sure to import the `sys` module and then add the path to the student file. Import the `unittest` module, the `circle_area` function from the student code, and `pi` from the `math` module. The test should be a subclass of `TestCase`. 

[Remove Highlighting](open_file .guides/secure/test_circle_area.py panel=0)

## Test the Output
[See the Output Test](open_file .guides/secure/test_circle_area.py panel=0 ref="def test_area" count=4)

Create several cases that test the end result of the student. Testing parameters like 0 and 1 are simple to do, but be sure to other numbers to verify the function is working as expected.

[Remove Highlighting](open_file .guides/secure/test_circle_area.py panel=0)

## Test Parameter Values
[See the Value Test](open_file .guides/secure/test_circle_area.py panel=0 ref="def test_values" count=2)

Circles cannot have a negative radius, so the student code should raise a value error when a negative number is passed to the function.

[Remove Highlighting](open_file .guides/secure/test_circle_area.py panel=0)

## Test Parameter Types
[See the Type Test](open_file .guides/secure/test_circle_area.py panel=0 ref="def test_types" count=4)

A circle's radius cannot be expressed as a string or boolean value. In addition, a radius must be a real number. In Python, `j` represents the square root of -1. Verify that the student code raises a type error when parameters are not a real number.

[Remove Highlighting](open_file .guides/secure/test_circle_area.py panel=0)