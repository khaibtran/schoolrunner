import attendanceFunc
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

courses = {
    '4266': {'name': 'UConn', 'enrolled': '0', 'marked': 0},
    '4269': {'name': 'Syracuse', 'enrolled': '0', 'marked': 0},
    '4270': {'name': 'Oxford', 'enrolled': '0', 'marked': 0},
    '4267': {'name': 'ULL', 'enrolled': '0', 'marked': 0},
    '4271': {'name': 'Mizzou', 'enrolled': '0', 'marked': 0},
    '4268': {'name': 'Tulane', 'enrolled': '0', 'marked': 0},
    '4272': {'name': 'Florida', 'enrolled': '0', 'marked': 0},
    '4273': {'name': 'UCSB', 'enrolled': '0', 'marked': 0},
    '4274': {'name': 'Oregon', 'enrolled': '0', 'marked': 0},
    '4276': {'name': 'PVU', 'enrolled': '0', 'marked': 0},
    '4275': {'name': 'LSU', 'enrolled': '0', 'marked': 0},
    '4279': {'name': 'UCLA', 'enrolled': '0', 'marked': 0},
    '4278': {'name': 'Stockton', 'enrolled': '0', 'marked': 0},
    '4277': {'name': 'TCNJ', 'enrolled': '0', 'marked': 0},
    '4282': {'name': 'Iowa', 'enrolled': '0', 'marked': 0},
    '4281': {'name': 'Washington', 'enrolled': '0', 'marked': 0},
    '4280': {'name': 'Howard', 'enrolled': '0', 'marked': 0},
    '4362': {'name': 'Arkansas', 'enrolled': '0', 'marked': 0},
    '4360': {'name': 'Auburn', 'enrolled': '0', 'marked': 0},
    '4361': {'name': 'Georgia', 'enrolled': '0', 'marked': 0},
    '4359': {'name': 'Tuskegee', 'enrolled': '0', 'marked': 0},
    '4358': {'name': 'Grambling', 'enrolled': '0', 'marked': 0},
    '4357': {'name': 'Southern', 'enrolled': '0', 'marked': 0},
    '4355': {'name': 'Harvard', 'enrolled': '0', 'marked': 0},
    '4265': {'name': 'Yale', 'enrolled': '0', 'marked': 0},
    '4356': {'name': 'Stanford', 'enrolled': '0', 'marked': 0},
    '4668': {'name': 'Missing Homeroom - 4668', 'enrolled': '0', 'marked': 0},
    '4716': {'name': 'Missing Homeroom - 4716', 'enrolled': '0', 'marked': 0}
}
attendanceFunc.getMissingAttendance(courses, params)
