# Partial Points with a Custom Test

## Writing the Test

### Points Variable

This is an example of a custom test with partial points. Be sure to [create a variable](open_file .guides/partial_points_custom.py panel=0 ref="points" count=1) called `points` which will be used to keep track of the points earned.

### Adding Points

In this particular example, there are six individual tests that run against the student code. If the student passes the test, `points` is incremented by 1. [Test 1.](open_file .guides/partial_points_custom.py panel=0 ref="Boarding test passed" count=2) [Test 2.](open_file .guides/partial_points_custom.py panel=0 ref="Fare test passed" count=2) [Test 3.](open_file .guides/partial_points_custom.py panel=0 ref="Disembark test passed" count=2) [Test 4.](open_file .guides/partial_points_custom.py panel=0 ref="Distance test passed" count=2) [Test 5.](open_file .guides/partial_points_custom.py panel=0 ref="Advance test passed" count=2) [Test 6.](open_file .guides/partial_points_custom.py panel=0 ref="Change fare test passed" count=2)

### Pass `points` to Codio

An advanced code test without partial points ends with a system exit of 0 (test passed) or 1 (test did not pass). Advanced code tests with partial points are different in that they end with an HTTP request that passes the `points` variable to Codio. Here is an example (taken from the [documentation](https://docs.codio.com/courses/assessments/#partial-score)) of how `points` would be passed to Codio.

```python
import os, requests, sys

points = 5
url = "{0}&points={1}".format(os.environ['CODIO_PARTIAL_POINTS_URL'], points)
r = requests.get(url)
```

Be sure to import the [appropriate modules](open_file .guides/partial_points_custom.py panel=0 ref="import sys" count=3). Using the example test on the right, passing the `points` variable takes place at the [end of the test](open_file .guides/partial_points_custom.py panel=0 ref="url" count=2).

## Adding the Assessment

Add an advanced code as shown in a previous lesson. Under the `EXECUTION` tab on the right, be sure to toggle `ALLOW PARTIAL POINTS`.

![Allow Partial Points](.guides/img/allow_partial_points.png)

Then under the `GRADING` tab, enter the total number of points for this code test. The points entered here should match the total number of points a student can earn in the advanced code test.

You advanced code test now has partial points and is ready to be shared with your students.
![Total Points](.guides/img/total_points.png)

