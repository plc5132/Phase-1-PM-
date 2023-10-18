import pandas as pd
import matplotlib.pyplot as plt

# Read the data from CSV files
forms = pd.read_csv('/Users/phebecornell/Desktop/Grad School/Project Management /Construction_Data_PM_Forms_All_Projects.csv')
tasks = pd.read_csv('/Users/phebecornell/Desktop/Grad School/Project Management /Construction_Data_PM_Tasks_All_Projects.csv')

# 1) Report the total number of tasks that are overdue
overdue_forms_count = forms[forms['overdue'] == True].shape[0]
overdue_tasks_count = tasks[tasks['overdue'] == True].shape[0]
total_overdue = overdue_forms_count + overdue_tasks_count
print(f"Total number of overdue tasks: {total_overdue}")

# 2) Report the total number of open and closed tasks by each task group
grouped_forms = forms.groupby(['report forms group', 'status']).size()
grouped_tasks = tasks.groupby(['task group', 'status']).size()
print("Total number of open and closed tasks by each forms group:")
print(grouped_forms)
print("Total number of open and closed tasks by each tasks group:")
print(grouped_tasks)

# 3) Create a bar chart of the total number of open and closed tasks by each task group
grouped_forms.unstack().plot(kind='bar')
plt.title('Open and Closed Tasks by Each Forms Group')
plt.xlabel('Group')
plt.ylabel('Count')
plt.show()

grouped_tasks.unstack().plot(kind='bar')
plt.title('Open and Closed Tasks by Each Tasks Group')
plt.xlabel('Group')
plt.ylabel('Count')
plt.show()

# 4) Create a bar chart of the total number of overdue tasks by project
overdue_forms_by_project = forms[forms['overdue'] == True].groupby('projects').size()
overdue_tasks_by_project = tasks[tasks['overdue'] == True].groupby('project').size()

overdue_forms_by_project.plot(kind='bar')
plt.title('Overdue Tasks by Project (Forms)')
plt.xlabel('Project')
plt.ylabel('Count')
plt.show()

overdue_tasks_by_project.plot(kind='bar')
plt.title('Overdue Tasks by Project (Tasks)')
plt.xlabel('Project')
plt.ylabel('Count')
plt.show()
