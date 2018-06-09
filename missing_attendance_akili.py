import attendanceFunc
import login
from datetime import date
"""
This is a basic example of a script that pulls data from Schoolrunner API (the
absences endpoint), then process the JSON results to print information about
absences for a specific student. This is just for demonstration purposes.

See http://docs.python-requests.org/en/master/ for documentation about how
the Requests library should be used.

See https://<yournetwork>.schoolrunner.org/api/doc/endpoints/ to see documentation
about the parameters that each endpoint supports and what the results look like.

Also use Postman to explore the results so that you know how the JSON results
can be manipulated.
"""

today = date.today().strftime("%Y-%m-%d")

# Parameters for the GET request
params = {
    'limit': '30000',
    'min_date': today,
    'max_date': today,
    'school_ids': '5,9' #Akili is 5 and 9
}

"""
Get total enrolled in class
"""

courses = login.akili_courses
attendanceFunc.getMissingAttendance(courses, params)
