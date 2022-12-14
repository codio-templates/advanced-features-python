# Testing Student Code

![Try It](.guides/img/try-it.png)

Students need the ability to run their code and check their work prior to submitting it for a grade. Link the unit test to the `TRY IT` button. This gives the student the full feedback from the unit test, but it does not send a grade to the LMS. In addition, the rationale and feedback will not be shown. Here's the code to use in the Guide. Notice that this button calls a bash script as opposed to a Python script. When the unit test is in `.guides`, it needs to be called from that directory.

```
{try it}(bash .guides/test_student_code.sh)
```

The bash script simply changes directory to the `.guides` directory and calls the Python unit test from there. Students will see the output from the test without affecting their grade.

```bash
#!/bin/bash

cd .guides
python3 -m unittest test_circle_area.py
```