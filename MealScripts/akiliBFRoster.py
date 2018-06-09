import csv
import json
import requests
import os, sys
sys.path.insert(0, '../')
import login
from datetime import date
from requests.auth import HTTPBasicAuth

workingDate = str(sys.argv[1])

user = login.user

pw = login.pw

network = login.network

school = "Akili"

total = 0

studentList = []

studentRoster = {}

params_students = {
    'school_ids': login.akili_school_id                             #School Ids for Akili
}

endpoint_students = 'students'

params_absences = {
    'min_date': workingDate,
    'max_date': workingDate,
    'school_ids': login.akili_school_id,
    'absence_type_ids': login.akili_attendance_id
}

params_tardy = {
    'min_date': workingDate,
    'max_date': workingDate,
    'school_ids': login.akili_school_id,
    'absence_type_ids': login.akili_tardy_id
}

endpoint_absences = 'absences'

with open('roster' + school + '.json', 'r') as file :
    data = json.load(file)
    

"""
This section checks for present with breakfast
"""
url = 'https://' + network + '.schoolrunner.org/api/v1/' + endpoint_absences
response = requests.get(url, auth=HTTPBasicAuth(user, pw), params=params_absences)
print response.request.url

presentStudents = response.json()
presentStudents = presentStudents['results']['absences']


#This for block cross checks for students who are present and rostered
for d, d_info in data.iteritems():
    for p in presentStudents:
        if d_info['students'].count(p['student_id']) > 0:
            studentList.append(p['student_id'])
            
"""
This section checks for tardy with breakfast
"""
urlTardy = 'https://' + network + '.schoolrunner.org/api/v1/' + endpoint_absences
responseTardy = requests.get(urlTardy, auth=HTTPBasicAuth(user, pw), params=params_tardy)
print responseTardy.request.url

tardyStudents = responseTardy.json()
tardyStudents = tardyStudents['results']['absences']

#This block checks for tardy students to see if they recived breakfast comment
for d, d_info in data.iteritems():
    for t in tardyStudents:
        if d_info['students'].count(t['student_id']) > 0 and t['comments'] == 'bf':
            studentList.append(t['student_id'])
            

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
    for s in studentList:
        if j['student_id'] == s:
            studentRoster[j['sis_id']] = {'lastname': j['last_name'], 'firstname': j['first_name']}
            total += 1

with open(school + '/' + workingDate + '_bf.csv', 'w') as output:
    writer = csv.writer(output, delimiter=',',lineterminator='\n')
    writer.writerow([workingDate, "Breakfast"])
    for sid in studentRoster:
            writer.writerow([sid, studentRoster[sid]['lastname'], studentRoster[sid]['firstname']])

print("Created file: " + workingDate + "_bf.csv")
print("Total records: " + str(total))
