import os
import subprocess
import sys

sys.path.append(os.path.join(os.getcwd(), ".guides", "secure"))
path = "student_code"
file = "custom_test.py"
student_code = os.path.join(path, file)
expected_output = "Hello world"

def count_prints(file):
  num_prints = 0
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if "print" in line:
        num_prints += 1
    
  return num_prints == 1

def check_output(file):
  student_output = subprocess.check_output(["python3", file]).rstrip()
  if student_output.decode("utf-8") == expected_output:
    return True
  else:
    return False
  
def count_variables(file):
  num_vars = 0
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if "=" in line:
        num_vars += 1
    
  return num_vars == 2

def no_empty_string(file):
  no_empty = True
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if '""' in line or "''" in line:
        no_empty = False
    
  return no_empty
  
def check_concat(file):
  has_concat = False
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if '+' in line:
        has_concat = True
    
  return has_concat
  
if not count_variables(student_code):
  print("<b>Test did not pass</b>")
  print("Program did not use two variables.")
  print("<hr>")

if not check_output(student_code):
  print("<b>Test did not pass</b>")
  print("Program did not print 'Hello world'.")
  print("<hr>")

if not count_prints(student_code):
  print("<b>Test did not pass</b>")
  print("Did not use one print statement.")
  print("<hr>")
  
if not no_empty_string(student_code):
  print("<b>Test did not pass</b>")
  print("Program should not contain any empty strings.")
  print("<hr>")
  
if not check_concat(student_code):
  print("<b>Test did not pass</b>")
  print("Program did not concatenate two strings.")
  print("<hr>")

if check_output(student_code) and count_variables(student_code) and no_empty_string(student_code) and count_prints(student_code) and check_concat(student_code):
  print("<h2>Test passed!</h2>")
  sys.exit(0)
else:
  sys.exit(1)