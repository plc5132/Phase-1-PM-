import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV files
forms = pd.read_csv('/Users/phebecornell/Desktop/Grad School/Project Management /Construction_Data_PM_Forms_All_Projects.csv')
tasks = pd.read_csv('/Users/phebecornell/Desktop/Grad School/Project Management /Construction_Data_PM_Tasks_All_Projects.csv')

# Report the total number of tasks that are overdue
overdue_forms_count = forms[forms['OverDue'] == 'True'].shape[0]
overdue_tasks_count = tasks[tasks['OverDue'] == 'True'].shape[0]

print(f"Total number of overdue forms: {overdue_forms_count}")
print(f"Total number of overdue tasks: {overdue_tasks_count}")

# Report the total number of open and closed tasks by each task group
task_group_status = tasks.groupby(['Task Group', 'Status']).size().unstack(fill_value=0)
print(task_group_status)

# Create a bar chart of the total number of open and closed tasks by each task group
task_group_status.plot(kind='bar')
plt.title('Total Number of Open and Closed Tasks by Task Group')
plt.xlabel('Task Group')
plt.ylabel('Total Number of Tasks')
plt.show()

# Create a bar chart of the total number of overdue tasks by project
overdue_by_project = tasks[tasks['OverDue'] == 'True'].groupby('project').size()
overdue_by_project.plot(kind='bar')
plt.title('Total Number of Overdue Tasks by Project')
plt.xlabel('Project')
plt.ylabel('Total Number of Overdue Tasks')
plt.show()
