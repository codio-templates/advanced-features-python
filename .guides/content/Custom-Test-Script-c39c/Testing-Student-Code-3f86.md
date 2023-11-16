
# Testing Student Code

Students should have the flexibility to test their code for errors before submitting it for grading. To support this, instructors can set up two distinct "try it" buttons: the first offers a swift syntax validation, while the second provides detailed feedback based on the grading criteria.

![Try It](.guides/img/try-it.png)

## Quick Test Button: 

This button lets students swiftly run their code, primarily checking for any syntax errors and viewing the output.

> **Note**: While this will show the basic output and syntax errors, it won't evaluate the code against specific criteria like the required number of `print` statements or variables usage.

**Add to Guide**: 
```bash
{try it}(python3 student_code/custom_test.py)
```

## Comprehensive Feedback Button: 

This button runs the grading script, providing comprehensive feedback similar to the advanced code test. Students will know where their code stands against the complete criteria but won't receive a grade in the LMS.

> **Tip**: The feedback won't render as HTML and won't show rationale details when run through this button.

### Options for the Comprehensive Feedback Button:

#### A: Modified Testing Script Outside the Secure Folder

To protect your main grading script, you can keep it in the `.guides/secure` folder but also create a modified, less detailed version of the script outside the secure folder. This allows students to get feedback without accessing the full criteria or sensitive grading details.

**Example Setup**:
1. Save the detailed grading script in `.guides/secure/custom_test_script.py`.
2. Create a modified version, e.g., `.guides/custom_feedback_script.py`.
3. Link to the modified script in your guide:

**Add to Guide**: 
```bash
{try it}(python3 .guides/custom_feedback_script.py)
```
#### B: If not Using Secure Folder

If you choose not to place your testing script in the `.guides/secure` folder, you can use the button directly:

**Add to Guide**: 
```bash
{try it}(python3 .guides/custom_test_script.py)
```

