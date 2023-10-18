import pandas as pd
import matplotlib.pyplot as plt

# Load your data
forms_df = pd.read_csv('/Users/phebecornell/Desktop/Grad School/Project Management /Construction_Data_PM_Forms_All_Projects.csv')
tasks_df = pd.read_csv('/Users/phebecornell/Desktop/Grad School/Project Management /Construction_Data_PM_Tasks_All_Projects.csv')

# Filter the data frames to include only the rows where 'OverDue' is True
forms_overdue = forms_df[forms_df['OverDue'] == True]
tasks_overdue = tasks_df[tasks_df['OverDue'] == True]

# Combine the two data frames into one
combined_df = pd.concat([forms_overdue, tasks_overdue])

# Group by 'Project' and sum the occurrences
grouped_by_project = combined_df.groupby('Project').size()

# Print the DataFrame to make sure it has data
print(grouped_by_project)

# Plot the data
if not grouped_by_project.empty:
    grouped_by_project.plot(kind='bar', figsize=(10, 6))
    plt.title('Total Number of Overdue Tasks by Project')
    plt.xlabel('Project')
    plt.ylabel('Number of Overdue Tasks')
    plt.show()
else:
    print("The DataFrame is empty. No data to plot.")


