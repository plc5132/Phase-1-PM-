import pandas as pd
import matplotlib.pyplot as plt

# Read the 'tasks' DataFrame from a CSV file
tasks_df = pd.read_csv('/Users/phebecornell/Desktop/Grad School/Project Management /Construction_Data_PM_Tasks_All_Projects.csv')  # Replace with your file path

# Filter the DataFrame to only include rows where 'Status' is 'Open' or 'Closed'
filtered_tasks = tasks_df[tasks_df['Status'].isin(['Open', 'Closed'])]

# Group the tasks by 'Task Group' and 'Status' and count them
grouped_by_group_and_status = filtered_tasks.groupby(['Task Group', 'Status']).size().unstack(fill_value=0)

# Plot the bar chart
grouped_by_group_and_status.plot(kind='bar', stacked=False, figsize=(12, 6))
plt.xlabel('Task Group')
plt.ylabel('Total Number of Tasks')
plt.title('Total Number of Open and Closed Tasks by Task Group')
plt.legend(title='Status')
plt.show()


