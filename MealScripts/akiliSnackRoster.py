import os, sys
sys.path.insert(0, '../')
import login

import mealRosterFunc

workingDate = str(sys.argv[1])

meal = "Snack"

school = "Akili"

params_behavior = {
    'min_date': workingDate,
    'max_date': workingDate,
    'demerit_type_ids': login.akili_snack                  #Supper for Akili
}

params_students = {
    'school_ids': login.akili_school_id,
    'active': '1'
}

params_absences = {
    'min_date': workingDate,
    'max_date': workingDate,
    'school_ids': login.akili_school_id,                  #Akili School IDs
    'absence_type_ids': login.akili_present_attendance_id         #Attendance Codes
}

mealRosterFunc.getMealRoster(workingDate, params_behavior, params_students, params_absences, meal, school)
