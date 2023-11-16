# Adding the Assessment

![Student View](.guides/img/unit-test.png)

Follow the steps below to add an advanced code test to the Guide.

## Assessments Menu
Click on the Assessments button to see all of the assessments that Codio provides. Select `Advanced Code Test`.

![image of assessments selection screen](https://global.codio.com/content/assessments.png)

## The General Section
Add a `Name` to your assessment. This will look like a "title" for the test. Leave some instructions for the student so they understand how to write their code to solve the problem.

![General Section](.guides/img/assessment-general.png)

## The Execution Section
Leave the `LANGUAGE TYPE` as `Python` and in the field `LANGUAGE ASSESSMENT SUBTYPE` select `UnitTest`. 

Use `ADD CASE:` to specify the python files containing UnitTest tests you would like to run.

Use `python3` for the execution of the unit test and set the working directory to that of your UnitTest scripts, in our case `.guides/secure`. 

Add the directory of the student code files being tested in the `STUDENT FOLDER` field.

 - **Optional**: Rather than completing the Student Folder field here, leave it blank and add the following lines of code in your script setup section: 
 ```python-hide-clipboard
 import sys
 sys.path.append("/home/codio/workspace/student_code/")
 ```

![Execution Section](.guides/img/unit-test-execution.png)

## The Grading Section
Enter the number of points for the problem. Toggle `DEFINED NUMBER OF ATTEMPTS` if you want to restrict students submissions. 

To give students immediate feedback, enable `SHOW RATIONALE TO STUDENT`. 
 - Fill in the box below with feedback you want to provide. 
 - Use [triple backticks](https://help.github.com/en/github/writing-on-github/creating-and-highlighting-code-blocks) to create a code block.
 - Toggle `ALLOW PARTIAL POINTS` if you want the question to have partial points.
> **Note**: When partial points is enabled for a UnitTest, the points will be divided equally by the number of tests. No modifications to the script are required.


![Grading Section](.guides/img/unit-test-grading.png)



## The Metadata Section
These assessments can be added to your organization's assessment library. Filling out the `Metadata` section with tags allows you and your colleagues to search for these assessments. 

![Metadata Section](.guides/img/assessment-metadata.png)

Click **Create** to complete the process.