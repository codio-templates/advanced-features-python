# The Unit Test Script Overview

**Purpose**: The unit test script is designed to validate the correctness of the student's code against a set of predefined test cases, ensuring that the code behaves as expected under various conditions.

- You can upload any existing unit test scripts to Codio.
- For security, scripts should be stored **in the `.guides/secure` folder** to prevent student access.

## 1. Setup

[See the Setup](open_file .guides/secure/test_circle_area.py panel=0 ref="import" count=3)

- **Import Statements**:
  - The `unittest` module is essential for defining test cases and running them as part of your test suite.
  - `from math import pi` is a required constant in this example.
  - `from circle import circle_area` pulls in the `circle_area` function from the student's code module named `circle`. This function is what the test cases will be evaluating to ensure it behaves and calculates as expected.


## 2. Defining Test Cases

[See the Test Cases](open_file .guides/secure/test_circle_area.py panel=0 ref="class TestCircleArea" count=13)

- **Test Case Structure**:
  - Create test methods within a `TestCase` subclass to check various aspects of the code.
  - Each method should test a specific behavior of the `circle_area` function.

<details>
<summary><strong>Test methods included:</strong></summary>

- `test_area`: Verifies that the area calculation is accurate for given radii.
- `test_values`: Ensures that passing a negative radius raises a `ValueError`.
- `test_types`: Confirms that the code raises a `TypeError` for inputs that are not real numbers, such as strings, booleans, or complex numbers (in Python, complex numbers use `j` to represent the square root of -1). 

</details>

## 3. Test Execution & Results

[Executes the Test](open_file .guides/secure/test_circle_area.py panel=0 ref="unittest.main" count=2)

- **Execution and Outcome**:
  - The `unittest.main()` function is called to run all the test methods.
  - If all tests pass, the student's code is deemed correct, otherwise, the specific failures are reported.

--- 

For more on the Python UnitTest framework, refer to the documentation [here](https://docs.python.org/3/library/unittest.html).