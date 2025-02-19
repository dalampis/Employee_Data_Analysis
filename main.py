import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

file_path = 'employees_updated.csv'
data = pd.read_csv(file_path)
print('The data that we want to analyze:')
print(data)
print()

grouped_avg1 = data.groupby('Department').agg({
    'Salary': 'mean',
    'EmpSatisfaction': 'mean'
}).reset_index()
print('The mean salary and mean employee satisfaction for each department:')
print(grouped_avg1)
print()

fig, ax1 = plt.subplots(figsize = (12, 6))

ax1.bar(grouped_avg1['Department'], grouped_avg1['Salary'], color = 'green', label = 'Averare Salary')
ax1.set_xlabel('Department')
ax1.set_ylabel('Average Salary', color = 'green')
ax1.tick_params(axis = 'y', labelcolor = 'green')

ax2 = ax1.twinx()
ax2.plot(grouped_avg1['Department'], grouped_avg1['EmpSatisfaction'], color = 'blue', marker = 's', label = 'Average Employee Satisfaction')
ax2.set_ylabel('Average Employee Satisfaction', color = 'blue')
ax2.tick_params(axis = 'y', labelcolor = 'blue')

plt.title('Average Salary and Employee Satisfaction by Department')
plt.tight_layout()
ax1.legend(loc = 'upper left')
ax2.legend(loc = 'upper right')

plt.show()

grouped_avg2 = data.groupby('PerformanceScore').agg({
    'Absences': 'mean'
}).reset_index()
print('The mean number of absences for each performance score category')
print(grouped_avg2)
print()

plt.figure(figsize = (12, 6))
sns.barplot(x = 'PerformanceScore', y = 'Absences', data = grouped_avg2, hue = 'PerformanceScore', palette = 'viridis')
plt.legend([], [])
plt.xlabel('Performance Score')
plt.ylabel('Average Number of Absences')
plt.title('Average number of absences for each performance score')
plt.show()

counts = data['Department'].value_counts()
print('the number of employees in each department:')
print(counts)
print()

sal_stats = data.groupby('Department')['Salary'].describe()
print('The salary statistics within each department:')
print(sal_stats)
print()

plt.figure(figsize = (12, 8))
colors = plt.cm.viridis(np.linspace(0, 1, len(counts)))
plt.pie(counts, labels = counts.index, colors = colors, autopct = '%1.1f%%', startangle = 140)
plt.title('Distribution of employees across different departments')
plt.show()







