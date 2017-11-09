import requests
from datetime import date
from requests.auth import HTTPBasicAuth

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

network = 'crescentcity'

user = 'habans.api@crescentcityschools.org'

pw = 'Mamba2017'

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

# Make the GET request and store the results in a variable called response
endpoint = 'class-absence-totals'
url = 'https://' + network + '.schoolrunner.org/api/v1/' + endpoint
response = requests.get(url, auth=HTTPBasicAuth(user, pw), params=params)

# See the full URL that was used- this can be helpful for debugging purposes
print response.request.url

# Decode the response to a JSON object that Python understands so that it
# can be accessed and manipulated like Python lists and dictionaries
json_data = response.json()

# Drill down from all data to the "results" stuff
# Reassign the json_data variable to this new subset of data
json_data = json_data['results']

# Drill down from "results" to the data for this specific endpoint
json_data = json_data['class_absence_totals']

#Set total enrolled students from endpoint
for j in json_data:
    if j['section_period_id'] in courses:
        courses[j['section_period_id']]['enrolled'] = j['enrolled_students']
    else:
        courses[j['section_period_id']] = {'name': ('WRONG SECTION - ' + j['section_period_id']), 'enrolled': j['enrolled_students'], 'marked': 0}


"""
Get current attendance for each student
"""

# Make the GET request and store the results in a variable called response
endpoint = 'class-absences'
url = 'https://' + network + '.schoolrunner.org/api/v1/' + endpoint
response = requests.get(url, auth=HTTPBasicAuth(user, pw), params=params)

# See the full URL that was used- this can be helpful for debugging purposes
print response.request.url

# Decode the response to a JSON object that Python understands so that it
# can be accessed and manipulated like Python lists and dictionaries
json_data = response.json()

# Drill down from all data to the "results" stuff
# Reassign the json_data variable to this new subset of data
json_data = json_data['results']

# Drill down from "results" to the data for this specific endpoint
json_data = json_data['class_absences']

# Loop through each of the records in json_data to process them
for j in json_data:
        courses[j['section_period_id']]['marked'] += 1

for c, c_info in sorted(courses.iteritems()):
    if c_info['marked'] != int(c_info['enrolled']):
        #print(c_info['name'].rjust(20, ' '))
        print(' MISSING '.center(30, '*') +'\n*' + ((c_info['name'].rjust(14, ' ') + ' ' + str(c_info['marked']) + '/' + c_info['enrolled'])).ljust(28, ' ') + '*\n' + ' '.rjust(31, '*'))
    elif c_info['marked'] == 0:
        print(' NOT TAKEN '.center(30, '#') +'\n#' + ((c_info['name'].rjust(14, ' ') + ' ' + str(c_info['marked']) + '/' + c_info['enrolled'])).ljust(28, ' ') + '#\n' + ' '.rjust(31, '#'))
    else :
        print(c_info['name'].rjust(15, ' ') + ' ' + str(c_info['marked']) + '/' + c_info['enrolled'])
