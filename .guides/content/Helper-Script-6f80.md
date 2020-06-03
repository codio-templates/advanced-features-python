# Helper Script

Helper scripts only apply to custom auto-grading scripts. If your code test is in the `.guides/secure` directory and you want to import a student-created function or class, then you will need a helper script. The helper script will make a copy of the student code and paste the file in the same directory as the helper script and test script. This way there will be no issues importing the code to be tested.

## Workflow

The Codio advanced code test should call the helper script, which copies/pastes the student code, then it calls the test script. Once the test script has run, it will use the system exit to return the points accrued by the student to the helper script, which will then use the HTTP request to pass the points to Codio.

## Test Script Example
The test script will stay almost the same as the test found on the `Custom Test` page from this chapter. However, the HTTP request will be replaced with a system exit. This will pass the number of points back to the helper script.

```python
# The rest of the code test remains the same

print("<b>~~~~~Tests~~~~~</b>")
boarding_test = check_boarding(test_subway, 200)
fare_test = check_fares(test_subway, 200)
exit_test = check_exit(test_subway)
distance_test = check_distance(test_subway, "Davis")
advance_test= check_advance(test_subway)
change_fare_test = check_change_fare(test_subway, 2.55)

# Replace the HTTP request with a system exit
sys.exit(points)
```

## Helper Script Example

This template (left) for a helper script can be applied to any advanced code test. Be sure that the variables `student_file` and `new_location` point to the correct directories. Also, verify that `result` is executing the proper command to run the copy of the student code. This helper script needs to import the `requests` module and replace the system exit with an HTTP request.
