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
