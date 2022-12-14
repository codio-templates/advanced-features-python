# Helper Script

If your code test is in the `.guides/secure` directory and you want to import a student-created function or class, then you will need a helper script. The helper script will make a copy of the student code and paste the file in the same directory as the helper script and test script. This way there will be no issues importing the code to be tested.

## Workflow

The Codio advanced code test should call the helper script, which copies the student code to the `.guides` directory, and then it calls the test script. Once the test script has run, it will use the system exit to return the 0 or 1 to the helper script, which will then use a system exit to return the 0 or 1 to Codio.

## Helper Script Example

This template for a helper script (left) can be applied to any advanced code test. Be sure that the variables `student_file` and `new_location` point to the correct directories. Also, verify that `result` is executing the proper command to run the copy of the student code.

