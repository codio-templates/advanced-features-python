import os, shutil, sys, requests

# location of the student file
student_file = "/path/to/student/file.py" 

# location of the code test
new_location = "/path/to/directory/with/code_test" 

# copy student file to the new location
shutil.copy(student_file, new_location)

# run the code test on student file
points = os.system("python3 .guides/path/to/grading_script.py") 

# HTTP request to pass the partial points back to Codio
url = "{0}&points={1}".format(os.environ['CODIO_PARTIAL_POINTS_URL'], points)
r = requests.get(url)
