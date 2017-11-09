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
    'school_ids': '7,8' #7 is Habans Pk-5 and 8 is 6-8
}

"""
Get total enrolled in class
"""

courses = {
    '4594': {'name': 'Brown', 'enrolled': '0', 'marked': 0},
    '4595': {'name': 'LSU', 'enrolled': '0', 'marked': 0},
    '4596': {'name': 'Loyola', 'enrolled': '0', 'marked': 0},
    '4614': {'name': 'Spelman', 'enrolled': '0', 'marked': 0},
    '4615': {'name': 'Stanford', 'enrolled': '0', 'marked': 0},
    '4616': {'name': 'Grambling', 'enrolled': '0', 'marked': 0},
    '4632': {'name': 'Michigan', 'enrolled': '0', 'marked': 0},
    '4633': {'name': 'NYU', 'enrolled': '0', 'marked': 0},
    '4634': {'name': 'Hampton', 'enrolled': '0', 'marked': 0},
    '4650': {'name': 'Haverford', 'enrolled': '0', 'marked': 0},
    '4651': {'name': 'Tulane', 'enrolled': '0', 'marked': 0},
    '4652': {'name': 'UC Santa Cruz', 'enrolled': '0', 'marked': 0},
    '4483': {'name': 'Tuskegee', 'enrolled': '0', 'marked': 0},
    '4482': {'name': 'Northwestern', 'enrolled': '0', 'marked': 0},
    '4521': {'name': 'Barat', 'enrolled': '0', 'marked': 0},
    '4572': {'name': 'Berkeley', 'enrolled': '0', 'marked': 0},
    '4573': {'name': 'Princeton', 'enrolled': '0', 'marked': 0},
    '4560': {'name': 'Columbia', 'enrolled': '0', 'marked': 0},
    '4561': {'name': 'Vanderbilt', 'enrolled': '0', 'marked': 0},
    '4522': {'name': 'UCLA', 'enrolled': '0', 'marked': 0},
    '4446': {'name': 'UNO', 'enrolled': '0', 'marked': 0},
    '4447': {'name': 'Xavier', 'enrolled': '0', 'marked': 0},
    '4520': {'name': 'Ohio State', 'enrolled': '0', 'marked': 0},
    '4448': {'name': 'MIT', 'enrolled': '0', 'marked': 0},
    '4449': {'name': 'Texas', 'enrolled': '0', 'marked': 0},
    '4450': {'name': 'Cornell', 'enrolled': '0', 'marked': 0},
    '4451': {'name': 'Howard', 'enrolled': '0', 'marked': 0},
    '4519': {'name': 'SELU', 'enrolled': '0', 'marked': 0},
    '4516': {'name': 'Morehouse', 'enrolled': '0', 'marked': 0},
    '4518': {'name': 'AmericanLS', 'enrolled': '0', 'marked': 0},
    '4517': {'name': 'AmericanUS', 'enrolled': '0', 'marked': 0},
    '4515': {'name': 'Aurora', 'enrolled': '0', 'marked': 0}
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
