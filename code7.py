import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have read your data into DataFrames
forms_df = pd.read_csv('/Users/phebecornell/Desktop/Grad School/Project Management /Construction_Data_PM_Forms_All_Projects.csv')
tasks_df = pd.read_csv('/Users/phebecornell/Desktop/Grad School/Project Management /Construction_Data_PM_Tasks_All_Projects.csv')


# Filter the rows where 'OverDue' is True for both data sets
forms_overdue = forms_df[forms_df['OverDue'] == True]
tasks_overdue = tasks_df[tasks_df['OverDue'] == True]

# Combine both DataFrames
combined_df = pd.concat([forms_overdue, tasks_overdue])

# Group by 'Project' and count the number of 'OverDue' tasks
grouped_by_project = combined_df.groupby('Project')['OverDue'].sum()

# Create the bar chart
grouped_by_project.plot(kind='bar', figsize=(10, 6))

plt.title('Total Number of Overdue Tasks by Project')
plt.xlabel('Project')
plt.ylabel('Number of Overdue Tasks')
plt.show()



