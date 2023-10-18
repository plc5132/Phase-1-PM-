import pandas as pd
import matplotlib.pyplot as plt

# Read your CSV files
forms = pd.read_csv('/Users/phebecornell/Desktop/Grad School/Project Management /Construction_Data_PM_Forms_All_Projects.csv')
tasks = pd.read_csv('/Users/phebecornell/Desktop/Grad School/Project Management /Construction_Data_PM_Tasks_All_Projects.csv')

# Debug: Print the columns
print("Columns in 'forms' DataFrame:", forms.columns)
print("Columns in 'tasks' DataFrame:", tasks.columns)

# 1) Report the total number of tasks that are overdue
overdue_forms_count = forms[forms['overdue'] == 'True'].shape[0]
overdue_tasks_count = tasks[tasks['overdue'] == 'True'].shape[0]
print(f"Total number of overdue forms: {overdue_forms_count}")
print(f"Total number of overdue tasks: {overdue_tasks_count}")

# 2) Report the total number of open and closed tasks by each task group
task_group_status = tasks.groupby(['task group', 'status']).size().unstack

