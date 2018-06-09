import attendanceFunc
import login
from datetime import date
import os, sys

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

if len(sys.argv) > 1:
    workingDate = str(sys.argv[1])
else:
    workingDate = date.today().strftime("%Y-%m-%d")

# Parameters for the GET request
params = {
    'limit': '30000',
    'min_date': workingDate,
    'max_date': workingDate,
    'school_ids': login.habans_school_id #7 is Habans Pk-5 and 8 is 6-8
}

"""
Get total enrolled in class
"""

courses = login.habans_courses

attendanceFunc.getMissingAttendance(courses, params)
