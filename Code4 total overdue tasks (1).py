import pandas as pd

# Read the CSV files for 'Forms' and 'Tasks'
forms = pd.read_csv('/Users/phebecornell/Desktop/Grad School/Project Management /Construction_Data_PM_Forms_All_Projects.csv')
tasks = pd.read_csv('/Users/phebecornell/Desktop/Grad School/Project Management /Construction_Data_PM_Tasks_All_Projects.csv')

# Count the number of overdue items in 'Forms'
overdue_forms_count = forms[forms['OverDue'] == True].shape[0]

# Count the number of overdue items in 'Tasks'
overdue_tasks_count = tasks[tasks['OverDue'] == True].shape[0]

# Print out the results
print(f"Total number of overdue forms: {overdue_forms_count}")
print(f"Total number of overdue tasks: {overdue_tasks_count}")
