import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files into pandas DataFrames
tasks_df = pd.read_csv('/Users/phebecornell/Desktop/Grad School/Project Management /Construction_Data_PM_Tasks_All_Projects.csv')
forms_df = pd.read_csv('/Users/phebecornell/Desktop/Grad School/Project Management /Construction_Data_PM_Forms_All_Projects.csv')

# Filter out the rows where the tasks and forms are not overdue
tasks_overdue = tasks_df[tasks_df['overdue'] == True]
forms_overdue = forms_df[forms_df['overdue'] == True]

# Combine the filtered DataFrames
combined_overdue_df = pd.concat([tasks_overdue, forms_overdue])

# Group by 'project' and count the number of overdue items
grouped_by_project = combined_overdue_df.groupby('project').size()

# Create the bar chart
plt.figure(figsize=(10, 6))
grouped_by_project.plot(kind='bar')
plt.title('Total Number of Overdue Tasks by Project')
plt.xlabel('Project')
plt.ylabel('Number of Overdue Tasks')
plt.show()


