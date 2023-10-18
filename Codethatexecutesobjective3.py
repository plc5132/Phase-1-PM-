import matplotlib.pyplot as plt
import numpy as np

# Data
task_groups = ['Design Team', 'Quality', 'Safety', 'Site Management']
closed_tasks = [728, 80, 4954, 1052]
open_tasks = [381, 191, 557, 297]

bar_width = 0.35  # width of the bars
index = np.arange(len(task_groups))  # label locations

# Create the bar chart
fig, ax = plt.subplots(figsize=(10, 6))

bar1 = ax.bar(index, closed_tasks, bar_width, label='Closed Tasks', color='b', alpha=0.7)
bar2 = ax.bar(index + bar_width, open_tasks, bar_width, label='Open Tasks', color='r', alpha=0.7)

# Function to add labels to the bars
def add_labels(bars, values):
    for bar, value in zip(bars, values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., height,
                '%d' % int(height), ha='center', va='bottom')

add_labels(bar1, closed_tasks)
add_labels(bar2, open_tasks)

# Describe the data
ax.set_xlabel('Task Group')
ax.set_ylabel('Number of Tasks')
ax.set_title('Number of Open and Closed Tasks by Task Group')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(task_groups)
ax.legend()

# Display the plot
plt.tight_layout()
plt.show()



