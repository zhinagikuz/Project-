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

# necessary variables
ind = np.arange(len(gender))
width = 0.35

rects1 = ax.bar(ind, male, width,
                color='#365e8c', )

rects2 = ax.bar(ind+width, female, width,
                    color='#8c364a')

# axes and labels

ax.set_ylim(0,10000) # Y axes values limit
ax.set_xlabel('Fiscal Years')
ax.set_ylabel('Number of Patients')
ax.set_title('Gender')
xTickMarks = [i for i in years]
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, fontsize=10)
plt.grid(True)

# add a legend
ax.legend( (rects1[0], rects2[0]), ('Male', 'Female') )

plt.show()

# close file gender.txt
file.close()
