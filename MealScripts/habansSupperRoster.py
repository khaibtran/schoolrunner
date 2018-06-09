import os, sys
sys.path.insert(0, '../')
import login

import mealRosterFunc

workingDate = str(sys.argv[1])

meal = "Supper"

school = "Habans"

params_behavior = {
    'min_date': workingDate,
    'max_date': workingDate,
    'demerit_type_ids': login.habans_supper                  #Snack for Habans
}

params_students = {
    'school_ids': login.habans_school_id,
    'active': '1'
}

params_absences = {
    'min_date': workingDate,
    'max_date': workingDate,
    'school_ids': login.habans_school_id,                  #Habans School IDs
    'absence_type_ids': login.habans_attendance_id + ',' + login.habans_tardy_id         #Attendance Codes
}

mealRosterFunc.getMealRoster(workingDate, params_behavior, params_students, params_absences, meal, school)
