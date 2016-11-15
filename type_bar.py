import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

# the data
# open file type.txt
file = open("type.txt","r")
drugs = []
y2555 = []
y2556 = []
y2557 = []
y2558 = []
for line in file:
    drugs.append(line.strip('\n').split())
for i in range(len(drugs)):
    drugs[i].pop(0)
y2555 = [int(i) for i in drugs[0]]
y2556 = [int(i) for i in drugs[1]]
y2557 = [int(i) for i in drugs[2]]
y2558 = [int(i) for i in drugs[3]]

n_groups = len(y2555)
 
# create plot
index = np.arange(n_groups) # data in list
bar_width = 0.2
 
rects1 = ax.bar(index, y2555, bar_width,
                 color='#8888F0',
                 label='2555')
 
rects2 = ax.bar(index + bar_width, y2556, bar_width,
                 color='#88F0BC',
                 label='2556')

rects3 = ax.bar(index + (bar_width*2), y2557, bar_width,
                 color='#F0BC88',
                 label='2557')
 
rects4 = ax.bar(index + (bar_width*3), y2558, bar_width,
                 color='#F088F0',
                 label='2558')

plt.title('Type of Drugs')
plt.xlabel('Drugs')
plt.ylabel('Total')
plt.xticks(index + bar_width*2, ('Heloin', 'Opium', 'Weed', 'Kratom', 'Sedative', 'Amphetamine', 'Narcotic', 'Alcohol', 'Volatile','Cigarette','Ice', 'Other','Unknown'))
plt.legend()

ax.set_xlim(-bar_width,len(index)+bar_width) # space margin left
plt.grid(True)

plt.show()

# close file gender.txt
file.close()
