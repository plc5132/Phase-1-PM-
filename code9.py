import pandas as pd
import matplotlib.pyplot as plt

# Read the 'tasks' DataFrame from a CSV file
tasks_df = pd.read_csv('/Users/phebecornell/Desktop/Grad School/Project Management /Construction_Data_PM_Tasks_All_Projects.csv')
print("Columns in tasks DataFrame:", tasks_df.columns)

# Filter the DataFrame to only include rows where 'OverDue' is True
tasks_overdue = tasks_df[tasks_df['OverDue'] == True]

# Group the overdue tasks by 'Project' and count them
grouped_by_project = tasks_overdue.groupby('Project').size()

# Check if the DataFrame is empty
if grouped_by_project.empty:
    print("The DataFrame is empty. No data to plot.")
else:
    # Plot the bar chart
    grouped_by_project.plot(kind='bar', figsize=(10, 6))
    plt.xlabel('Project')
    plt.ylabel('Total Number of Overdue Tasks')
    plt.title('Total Number of Overdue Tasks by Project')
    plt.show()
