# Partial Points with a Unit Test

**Purpose**: When integrating partial points with a Python unit test, the test creation process remains unchanged. However, the method of assigning points within the Codio Guide differs slightly to accommodate partial credit.

## Implementing the Test

Develop your unit test as you would typically, following the guidelines in the "Unit Test" section. The modification for partial points comes into play when you add the test to your Guide:

- In the **Grading Tab** of the assessment, toggle on `ALLOW PARTIAL POINTS` to enable partial credit for the test.

![Python Unit Test Partial Points](.guides/img/unit-test-partial-points.png)

Scores are computed based on the proportion of successful tests. The total points available are multiplied by this percentage to determine the student's score.

Consider the provided Python unit test example. It comprises three distinct tests:
- `test_area` and `test_types` each contain three assertions.
- `test_values` has a single assertion.

For a test to be considered passed, all its assertions must evaluate to true. Failing even one assertion in a test means no points are awarded for that test.

## Strategic Test Segmentation

The structuring of your tests will directly influence how points are awarded. In the example below, all assertions are part of a single test method:

```python
def test_area(self):
  self.assertAlmostEqual(circle_area(1), pi)
  self.assertAlmostEqual(circle_area(0), 0)
  self.assertAlmostEqual(circle_area(2.1), pi * 2.1 ** 2)
```

If a student's submission passes the first two assertions but fails the third, they would not earn any points for this test. The successful assertions do not contribute to their score.

To enable partial credit for each portion of the test they pass, you can divide the test into smaller, discrete tests:

```python
def test_area1(self):
  self.assertAlmostEqual(circle_area(1), pi)
  
def test_area2(self):
  self.assertAlmostEqual(circle_area(0), 0)
  
def test_area3(self):
  self.assertAlmostEqual(circle_area(2.1), pi * 2.1 ** 2)
```

This approach allows students to receive credit for each assertion passed, providing a more nuanced assessment of their understanding and skills.