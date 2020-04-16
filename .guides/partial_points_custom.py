import sys
import os
import requests
from exercise5 import Subway

points = 0
test_subway = Subway()

boarding_test = False
fare_test = False
exit_test = False
distance_test = False
advance_test = False
change_fare_test = False

def check_boarding(subway, new_passengers):
  """Verify that passengers board as expected"""
  subway.board(new_passengers)
  if subway.passengers == new_passengers:
    print('Boarding test passed')
    points += 1
    return True
  else:
    print("<b>Boarding test did not pass</b>")
    return False

def check_fares(subway, total_passengers):
  """Verify that fares are being tallyed"""
  if subway.total_fares == total_passengers * Subway.fare:
    print("<b>Fare test passed</b>")
    points += 1
    return True
  else:
    print("<b>Fare test did not pass</b>")
    return False

def check_exit(subway):
  """Verify that passengers are exiting as expected"""
  test1 = False
  test2 = False
  subway.disembark(75)
  if subway.passengers == 125:
    test1 = True
  subway.disembark(1000)
  if subway.passengers == 0:
    test2 = True
  if test1 and test2:
    print("<b>Disembark test passed</b>")
    points += 1
    return True
  else:
    print("<b>Disembark test did not pass</b>")
    return False

def check_distance(subway, desired_stop):
  """Verify that is being calculated as expected"""
  subway.current_stop = "Central"
  if subway.distance(desired_stop) == 3:
    print("<b>Distance test passed</b>")
    points += 1
    return True
  else:
    print("<b>Distance test did not pass</b>")
    return False
  
def check_advance(subway):
  """Verify that the subway is advancing as expected"""
  test1 = False
  test2 = False
  subway.advance()
  if subway.current_stop == "Kendall" and subway.direction == "south":
    test1 = True
  subway.current_stop = "Alewife"
  subway.direction = "north"
  subway.advance()
  if subway.current_stop == "Davis" and subway.direction == "south":
    test2 = True
  if test1 and test2:
    print("<b>Advance test passed</b>")
    points += 1
    return True
  else:
    print("<b>Advance test did not pass</b>")
    return False

def check_change_fare(subway, new_fare):
  """Verify that changing the fare affects all instances of the Subway class"""
  subway.change_fare(new_fare)
  if Subway.fare == new_fare:
    print("<b>Change fare test passed</b>")
    points += 1
    return True
  else:
    print("<b>Change fare test did not pass</b>")
    return False
  
print("<b>~~~~~Tests~~~~~</b>")
boarding_test = check_boarding(test_subway, 200)
fare_test = check_fares(test_subway, 200)
exit_test = check_exit(test_subway)
distance_test = check_distance(test_subway, "Davis")
advance_test= check_advance(test_subway)
change_fare_test = check_change_fare(test_subway, 2.55)

url = "{0}&points={1}".format(os.environ['CODIO_PARTIAL_POINTS_URL'], points)
r = requests.get(url)