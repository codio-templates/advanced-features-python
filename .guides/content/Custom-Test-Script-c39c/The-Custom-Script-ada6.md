# The Custom Script Breakdown
**Purpose**: The custom script evaluates student code for specific requirements and provides feedback. If the student code meets all requirements, it passes; otherwise, it points out areas where the student went wrong.

 - You can upload any grading scripts you already have to Codio. 
 - Scripts should be kept **in the `.guides/secure` folder** so that students do not have access to them.

|||important
## Student Access Restrictions

When provided access to the file tree, students can navigate through files and folders in the workspace. 

The `.guides` folder in its contents will **not** be available to them in the file tree, though students **can** access the `.guides` folder and its contents by navigating from the terminal.

If you store grading scripts in the `.guides/secure` folder, they run securely and students cannot see the script or the files in the folder. Only instructors can access this folder. You can find more information about assessment security [here](https://docs.codio.com/instructors/authoring/assessments/assessment-security.html#assessment-security).

> **Note**: You will need to create this folder in your assignment.

|||

## 1. Setup

[See Setup](open_file .guides/secure/custom_test_script.py panel=0 ref="import" count=9)

- **Modules Used**:
  - `os`: To interact with the OS, particularly to create a file path to the student code and manipulate the system path.
  - `subprocess`: To run external commands; here, it's used to run the student's code.
  - `sys`: To interact with the Python interpreter. It's used both for sending the exit code to Codio and appending the directory to the system path.

- **Key Variables**:
  - `path` & `file`: These identify where the student's code is and what it's named.
  - `student_code`: A full path to the student's code.
  - `expected_output`: The desired result from running the student's code.

> **Note**: Line 5 appends the system path with the `.guides/secure` directory to ensure any modules or files within it can be accessed. This is especially important as the testing script will be placed in this secure folder which student containers do not have access to. If you choose not to use the `secure` folder for your testing scripts, this line should be omitted.

## 2. Functions for Code Evaluation

[See Functions](open_file .guides/secure/custom_test_script.py panel=0 ref="def" count=42)

Each function returns a boolean value and tests an aspect of the student code. The number of functions for your grading script will depend on the number of aspects you are evaluating from the student code.

<details>
<summary><strong>The functions in this script:</strong></summary>

- `count_prints`: Checks if the student used exactly one `print` statement.
- `check_output`: Compares the student's output to the expected output.
- `count_variables`: Verifies that two variables were used.
- `no_empty_string`: Ensures no empty strings (`""` or `''`) exist in the code.
- `check_concat`: Checks if the student concatenated two strings.

</details>


## 3. Feedback Generation

[See Feedback](open_file .guides/secure/custom_test_script.py panel=0 ref="if not" count=24)

- Each function is invoked individually.
- If a function returns `False`, feedback is given to the student pinpointing the area they missed.
- The script allows for HTML rendering in feedback, enabling more formatted, visually clear feedback (e.g., bold text or horizontal rules).


## 4. Concluding & Sending Results

[See Result](open_file .guides/secure/custom_test_script.py panel=0 ref="if check" count=5)

- If all functions return `True`, it means the student's code has passed all checks. A success message is displayed.
- `sys.exit(0)` signals that the student's solution is correct, while `sys.exit(1)` indicates an incorrect solution.
