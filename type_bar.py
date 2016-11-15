import numpy as np
import matplotlib.pyplot as plt

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

# data to plot
n_groups = len(y2555)
 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.2
 
rects1 = plt.bar(index, y2555, bar_width,
                 color='#b23737',
                 label='2555')
 
rects2 = plt.bar(index + bar_width, y2556, bar_width,
                 color='#81b237',
                 label='2556')

rects3 = plt.bar(index + (bar_width*2), y2557, bar_width,
                 color='#3791b2',
                 label='2557')
 
rects4 = plt.bar(index + (bar_width*3), y2558, bar_width,
                 color='#5237b2',
                 label='2558')

plt.xlabel('Drugs')
plt.ylabel('Total')
plt.title('Type of Drugs')
plt.xticks(index + bar_width*2, ('heloin', 'opium', 'weed', 'kratom', 'sedative', 'amphetamine', 'narcotic', 'alcohol', 'volatile','cigarette','ice', 'other','unknown'))
plt.legend()
 
plt.tight_layout()
plt.show()

# close file gender.txt
file.close()
