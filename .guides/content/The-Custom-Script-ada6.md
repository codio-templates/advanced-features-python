# The Custom Script

You can upload any scripts you already have to Codio. Scripts should be kept in the `.guides` folder so that students do not have access to them.

## Setup

[See Setup](open_file .guides/custom_test_script.py panel=0 ref="import" count=8)

The `os` module is used to create a file path to the student code, the `subprocess` module is used to run the student code, and the `sys` module is used to send the exit code to Codio.

The `path` variable contains the path to the student code, and the `file` variable contains the name of the student file. These two values are combined to create the `student_code` variable, which is used later on in the program. The `expected_ouput` variable should contain the expected output of what the student code should produce.

## Functions

[See Functions](open_file .guides/custom_test_script.py panel=0 ref="def" count=33)

Each function returns a boolean value and tests an aspect of the student code. One function that will always be there is `check_output`. The number of other functions and their specifics depend on the coding problem.

## Feedback

[See Feedback](open_file .guides/custom_test_script.py panel=0 ref="if not" count=24)

Each function above is called separately. If they return `False`, then feedback should be given to the student as to why their code did not pass the code test. Output from `print` statements is rendered in the Guide, which is displayed on a webpage. So printing HTML tags will output HTML.

## Returning the Result

[See Result](open_file .guides/custom_test_script.py panel=0 ref="if check" count=5)

If all of the above the functions return `True`, then the student code is correct. A system exit of `0` lets Codio know that the solution is correct. A system exit of `1` tells Codio that the student code is incorrect.