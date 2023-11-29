# Partial Points with a Custom Test

**Purpose**: Implementing custom tests with partial points allows for granular assessment of student submissions, offering credit for each correctly implemented part of the assignment.

## 1. Import Testing Module

Begin by importing the [necessary modules for partial points grading](open_file .guides/partial_points_custom.py panel=0 ref="import sys" count=3):

- **System Path Modification**: Modify the system path if your test script resides outside the standard directories. This ensures the test script can access student submissions located in different folders.
- **Grading Module Import**: Use `send_partial_v2` from the grading library to transmit the results and feedback to Codio. This function allows you to send feedback in various formats: `FORMAT_V2_MD` for Markdown, `FORMAT_V2_HTML` for HTML, and `FORMAT_V2_TXT` for plain text.

> **Note**: `send_partial_v2` is a library specific to Python. If you are using other languages refer to the [documentation](https://docs.codio.com/instructors/authoring/assessments/partial-points.html#autograding-enhancements-for-partial-points).


[Remove highlighting](open_file .guides/partial_points_custom.py panel=0)

## 2. Setting up Variables for Testing

Establish variables to [track points](open_file .guides/partial_points_custom.py panel=0 ref="points" count=1) and [collect feedback](open_file .guides/partial_points_custom.py panel=0 ref="feedback" count=1):

- `points`: A counter for the points accrued by the student's code during testing.
- `feedback`: A string that accumulates feedback messages to be displayed to the student.

[Remove highlighting](open_file .guides/partial_points_custom.py panel=0)

## 3. Conducting the Tests

Design each test to evaluate specific aspects of students' code:

- **Points Allocation**: Assign a value to each test relative to its importance. If a test is passed, increment the `points` variable accordingly.
  - [Test 1.](open_file .guides/partial_points_custom.py panel=0 ref="Boarding test passed" count=2) [Test 2.](open_file .guides/partial_points_custom.py panel=0 ref="Fare test passed" count=2) [Test 3.](open_file .guides/partial_points_custom.py panel=0 ref="Disembark test passed" count=2) [Test 4.](open_file .guides/partial_points_custom.py panel=0 ref="Distance test passed" count=2) [Test 5.](open_file .guides/partial_points_custom.py panel=0 ref="Advance test passed" count=2) [Test 6.](open_file .guides/partial_points_custom.py panel=0 ref="Change fare test passed" count=2)
- **Feedback Assembly**: For tests that fail, append a descriptive feedback message to the `feedback` variable. This feedback will be presented to the student at the end of the testing process.
  - Decide on the format for your feedback (HTML, markdown, or text) and be sure to [import it](open_file .guides/partial_points_custom.py panel=0 ref="from lib.grade" count=1). Although line 3 of the script imports all three formats, this example uses HTML.
  - [Feedback 1.](open_file .guides/partial_points_custom.py panel=0 ref="Boarding test feedback" count=2) [Feedback 2.](open_file .guides/partial_points_custom.py panel=0 ref="Fare test feedback" count=2) [Feedback 3.](open_file .guides/partial_points_custom.py panel=0 ref="Disembark test feedback" count=2) [Feedback 4.](open_file .guides/partial_points_custom.py panel=0 ref="Distance test feedback" count=2) [Feedback 5.](open_file .guides/partial_points_custom.py panel=0 ref="Advance test feedback" count=2) [Feedback 6.](open_file .guides/partial_points_custom.py panel=0 ref="Change fare test feedback" count=2)
  - If `feedback` is [still an empty string](open_file .guides/partial_points_custom.py panel=0 ref="passing feedback" count=3) by the end of the test, add a message that the test has passed.

[Remove highlighting](open_file .guides/partial_points_custom.py panel=0)

## 4. Returning Results to Codio

Instead of a binary pass/fail outcome, use `send_partial_v2` to send a detailed result back to Codio for Advanced code tests with partial points enabled:

- **Result Submission**: Send the accumulated `points` and `feedback` to Codio using the [Codio library call](open_file .guides/partial_points_custom.py panel=0 ref="send results to Codio" count=2)  to make an HTTP request.
- **Formatting Feedback**: Decide on the feedback format (`FORMAT_V2_MD`, `FORMAT_V2_HTML`, or `FORMAT_V2_TXT`) and ensure it is consistently used throughout the test script.

[Remove highlighting](open_file .guides/partial_points_custom.py panel=0)

## 5. Assessment Configuration in Codio

When creating the advanced code test, modify the following in the **Grading Tab**: 
- Input the maximum number of points available for the code test.
- Toggle the `ALLOW PARTIAL POINTS` option to enable partial credit for the assessment.

![Allow Partial Points](.guides/img/allow-partial-points.png)

Now your advanced code test is configured to award partial points, offering a more nuanced evaluation of student work.
