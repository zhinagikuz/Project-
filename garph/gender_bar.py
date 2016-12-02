import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

# the data
# open file gender.txt
file = open("gender.txt","r")
gender = []
years = []
male = []
female = []
for line in file:
    gender.append(line.strip('\n').split())
for lst in gender:
    years.append(int(lst[0]))
    male.append(int(lst[1]))
    female.append(int(lst[2]))

n_groups = len(gender)

# create plot
index = np.arange(n_groups) # data in list
bar_width = 0.35

rects1 = ax.bar(index, male, bar_width,
                color='#365e8c',
                label = 'Male')

rects2 = ax.bar(index + bar_width, female, bar_width,
                color='#8c364a',
                label = 'Female')

plt.title('Gender')
plt.xlabel('Fiscal Years')
plt.ylabel('Number of Patients')
plt.xticks(index + bar_width, ('2555', '2556', '2557', '2558'))
plt.legend()

ax.set_xlim(-bar_width, len(index) + bar_width)
plt.grid(True)

plt.show()

# close file gender.txt
file.close()
