import requests
from datetime import date
from requests.auth import HTTPBasicAuth

today = date.today().strftime("%Y-%m-%d")

network = 'crescentcity'

user = 'habans.api@crescentcityschools.org'

pw = 'Mamba2017'

def getMissingAttendance(courses, params):

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
        if c_info['marked'] < int(c_info['enrolled']):
            print(' MISSING '.center(30, '*') +'\n*' + ((c_info['name'].rjust(14, ' ') + ' ' + str(c_info['marked']) + '/' + c_info['enrolled'])).ljust(28, ' ') + '*\n' + ' '.rjust(31, '*'))
        elif c_info['marked'] == 0:
            print(' NOT TAKEN '.center(30, '#') +'\n#' + ((c_info['name'].rjust(14, ' ') + ' ' + str(c_info['marked']) + '/' + c_info['enrolled'])).ljust(28, ' ') + '#\n' + ' '.rjust(31, '#'))
        else :
            print(c_info['name'].rjust(15, ' ') + ' ' + str(c_info['marked']) + '/' + c_info['enrolled'])
