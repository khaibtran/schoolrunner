from datetime import date
import mealReportFunc
import os, sys
sys.path.insert(0, '../')
import login

if len(sys.argv) > 1:
    workingDate = str(sys.argv[1])
else:
    workingDate = date.today().strftime("%Y-%m-%d")

params_behavior = {
    'limit': '30000',
    'min_date': workingDate,
    'max_date': workingDate,
    'demerit_type_ids': login.habans_supper #Snack for Habans
}

school = "Habans"

meal = "Supper"

mealReportFunc.getMealReport(workingDate, params_behavior, school, meal)

