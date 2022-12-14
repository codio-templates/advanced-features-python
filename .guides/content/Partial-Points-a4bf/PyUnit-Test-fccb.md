# Partial Points with a Unit Test

## Writing the Test

There are no changes to a Python unit test if it is using partial points. Create the test as normal, and add it to the Guide as indicated in the "Unit Test" section. The only change happens when adding the unit test to the Guide. Toggle the switch to allow for partial points. Then set the number of points for the assessment in the `GRADING` section.

![Python Unit Test Partial Points](.guides/img/unit_test_partial_points.png)

When using partial points, a student's score is calculated by the percentage of tests passed multiplied by the total number of points.

To the left is the Python unit test from before. There are three tests. `test_area` and `test_types` have three assert statements. All of these asserts must be true in order for the test to pass. `test_values` only has one assert statement; pass that and points will be assigned to the student.

## Test Design

How the test is designed affects how students are evaluated. In the test below, the student must pass the three assert statements to pass the test.

```python
def test_area(self):
  self.assertAlmostEqual(circle_area(1), pi)
  self.assertAlmostEqual(circle_area(0), 0)
  self.assertAlmostEqual(circle_area(2.1), pi * 2.1 ** 2)
```

If the student passes the first two asserts but fails the third, then they would receive no points for this test. The student would not get credit for the assert statements they did pass.

Rewriting the above test as three smaller tests would give the student credit for each assert statement they pass.

```python
def test_area1(self):
  self.assertAlmostEqual(circle_area(1), pi)
  
def test_area2(self):
  self.assertAlmostEqual(circle_area(0), 0)
  
def test_area3(self):
  self.assertAlmostEqual(circle_area(2.1), pi * 2.1 ** 2)
```