import csv
import json
import requests
import os, sys
sys.path.insert(0, '../')
import login
from datetime import date
from requests.auth import HTTPBasicAuth

def getMealRoster(workingDate, params_behavior, params_students, params_absences, meal, school):

    user = login.user

    pw = login.pw

    network = login.network

    total = 0

    studentList = []

    studentRoster = {}

    endpoint_behavior = 'behaviors'

    endpoint_students = 'students'

    endpoint_absences = 'absences'


    with open('roster' + school + '.json', 'r') as file :
        data = json.load(file)

    url = 'https://' + network + '.schoolrunner.org/api/v1/' + endpoint_behavior
    response = requests.get(url, auth=HTTPBasicAuth(user, pw), params=params_behavior)
    print response.request.url

    allStudentsSnack = response.json()
    allStudentsSnack = allStudentsSnack['results']['behaviors']

    url = 'https://' + network + '.schoolrunner.org/api/v1/' + endpoint_absences
    response = requests.get(url, auth=HTTPBasicAuth(user, pw), params=params_absences)
    print response.request.url

    presentStudents = response.json()
    presentStudents = presentStudents['results']['absences']

    """
    This for block cross checks for students who are present and also for duplicates
    """
    for a in allStudentsSnack:
        for p in presentStudents:
            if studentList.count(a['student_id']) == 0 and p['student_id'] == a['student_id']:
                studentList.append(a['student_id'])

    url = 'https://' + network + '.schoolrunner.org/api/v1/' + endpoint_students
    response = requests.get(url, auth=HTTPBasicAuth(user, pw), params=params_students)
    print response.request.url

    json_data = response.json()
    json_data = json_data['results']['students']

    """
    This for block checks to see if a student is in the roster. If not, do not write
    to file. This is to not print Aurora students
    """
    for j in json_data:
        for c, c_info in data.iteritems():
            if studentList.count(j['student_id']) > 0 and c_info['students'].count(j['student_id']) > 0:
                studentRoster[j['sis_id']] = {'lastname': j['last_name'], 'firstname': j['first_name']}
                total += 1

    with open(school + '/' + workingDate + '_' + meal +'.csv', 'wb') as output:
        writer = csv.writer(output, delimiter=',',lineterminator='\n')
        writer.writerow([workingDate, meal])
        for sid in studentRoster:
                writer.writerow([sid, studentRoster[sid]['lastname'], studentRoster[sid]['firstname']])

    print("Created file: " + workingDate + '_' + meal +'.csv')
    print("Total records: " + str(total))
