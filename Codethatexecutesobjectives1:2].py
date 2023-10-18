import pandas as pd

# Load the tasks DataFrame
tasks = pd.read_csv('/Users/phebecornell/Desktop/Grad School/Project Management /Construction_Data_PM_Tasks_All_Projects.csv')

# Group by 'Task Group' and 'Status' and count the number of occurrences
task_group_status_count = tasks.groupby(['Task Group', 'Status']).size().unstack(fill_value=0)

# Export the data to a CSV file
task_group_status_count.to_csv("grouped_tasks.csv")

# Print the DataFrame as a string-formatted table
print(task_group_status_count.to_string())
