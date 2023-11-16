# Updated Partial Points with a Custom Test

**Purpose**: The updated auto-grading script is designed to efficiently and securely evaluate student submissions in Codio, directly from the `.guides/secure` directory while accessing student code located outside this secure environment.

 > **Note**: This guide focuses on additional configurations and modifications necessary for running the script in the `.guides/secure` directory. It complements the information provided on the previous page and does not repeat the general details of the script's functionality and structure. For comprehensive script details, refer to the previous page.

## Key Aspects of the Updated Script

### Direct Integration with Student Code

- **Path Modification**: The script [appends the path to the student's code directory](open_file .guides/secure/partial_points_custom_secure.py panel=0 ref="Student Code" count=3) to `sys.path`. This adjustment allows the secure auto-grading script to import and interact directly with student submissions, even though the student code resides outside the secure directory.

[Remove highlighting](open_file .guides/secure/partial_points_custom_secure.py panel=0)

### Global Variable Declaration

- **Scope Management**: The script includes [declarations of `points` and `feedback` as global variables](open_file .guides/secure/partial_points_custom_secure.py panel=0 ref="def" count=93) within each function where they are modified, as seen on lines 24, 37, 49, and so on. This ensures correct scope management and avoids common errors associated with variable referencing in Python.

[Remove highlighting](open_file .guides/secure/partial_points_custom_secure.py panel=0)
