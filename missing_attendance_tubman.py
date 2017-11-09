from datetime import date
import attendanceFunc

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
    'school_ids': '2,6' #Tubman is 5 and 9
}

"""
Get total enrolled in class
"""

courses = {
    '4484': {'name': 'Clara Little Lambs', 'enrolled': '0', 'marked': 0},
    '4481': {'name': 'Aurora', 'enrolled': '0', 'marked': 0},
    '4137': {'name': 'Tulane', 'enrolled': '0', 'marked': 0},
    '4138': {'name': 'LSU', 'enrolled': '0', 'marked': 0},
    '4139': {'name': 'UMiami', 'enrolled': '0', 'marked': 0},
    '4140': {'name': 'UNC', 'enrolled': '0', 'marked': 0},
    '4141': {'name': 'Morehouse', 'enrolled': '0', 'marked': 0},
    '4142': {'name': 'Vanderbilt', 'enrolled': '0', 'marked': 0},
    '4378': {'name': 'TCU', 'enrolled': '0', 'marked': 0},
    '4215': {'name': 'Scripps', 'enrolled': '0', 'marked': 0},
    '4444': {'name': 'Oregon', 'enrolled': '0', 'marked': 0},
    '4223': {'name': 'Stanford', 'enrolled': '0', 'marked': 0},
    '4443': {'name': 'UWash', 'enrolled': '0', 'marked': 0},
    '4445': {'name': 'UCSC', 'enrolled': '0', 'marked': 0},
    '4385': {'name': 'Xavier', 'enrolled': '0', 'marked': 0},
    '4231': {'name': 'Wesleyan', 'enrolled': '0', 'marked': 0},
    '4232': {'name': 'Northwestern', 'enrolled': '0', 'marked': 0},
    '4375': {'name': 'Kenyon', 'enrolled': '0', 'marked': 0},
    '4241': {'name': 'Wisconsin', 'enrolled': '0', 'marked': 0},
    '4242': {'name': 'Notre Dame', 'enrolled': '0', 'marked': 0},
    '4374': {'name': 'Mizzou', 'enrolled': '0', 'marked': 0},
    '4251': {'name': 'UPenn', 'enrolled': '0', 'marked': 0},
    '4252': {'name': 'Howard', 'enrolled': '0', 'marked': 0},
    '4376': {'name': 'Fordham', 'enrolled': '0', 'marked': 0},
    '4261': {'name': 'Haverford', 'enrolled': '0', 'marked': 0},
    '4262': {'name': 'UConn', 'enrolled': '0', 'marked': 0},
    '4392': {'name': 'Rutgers', 'enrolled': '0', 'marked': 0}
}

attendanceFunc.getMissingAttendance(courses, params)
