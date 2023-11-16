# Adding the Style Checker

![Student View](.guides/img/style-student-view.png)

Follow the steps below to add a style checker inside an advanced code test to the Guide.


## Assessments Menu
Click on the Assessments button to see all of the assessments that Codio provides. Select `Advanced Code Test`.

![image of assessments selection screen](https://global.codio.com/content/assessments.png)

## The General Section
Add a `Name` to your assessment. This will look like a "title" for the test. Leave some instructions for the student so they understand how to write their code to solve the problem.

![General Section](.guides/img/style-general.png)

## The Execution Section
Set the `LANGUAGE TYPE` as `Python`. 

In the field `LANGUAGE ASSESSMENT SUBTYPE` select `PyCodeStyle`. 

In the field `ADD CASE` type the path to the student file, or simply drag the file into the field from the file tree. Click the button `ADD CASE`. The student file should appear below the field. 
 - You can add multiple files to check if need be.

![Execution Section](.guides/img/style-execution.png)

## The Grading Section
Enter the number of points for the problem. Toggle `DEFINED NUMBER OF ATTEMPTS` if you want to restrict students submissions. 

To give students immediate feedback, enable `SHOW RATIONALE TO STUDENT`. 
 - Fill in the box below with feedback you want to provide. 
 - Use [triple backticks](https://help.github.com/en/github/writing-on-github/creating-and-highlighting-code-blocks) to create a code block.


![Grading Section](.guides/img/style-grading.png)

> **Note**: Partial Points is not an option with PyCodeStyle.

## The Metadata Section
These assessments can be added to your organization's assessment library. Filling out the `Metadata` section with tags allows you and your colleagues to search for these assessments. 

![Metadata Section](.guides/img/assessment-metadata.png)

Click **Create** to complete the process.