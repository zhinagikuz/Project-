import matplotlib.pyplot as plt

# the data
# open file gender.txt
file = open("gender.txt", "r")
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

# plot line graph
plt.plot(years, male, color='#365e8c',label='Male', linewidth=2.5, marker='o') # (x,y)
plt.plot(years, female, color='#8c364a', label='Female', linewidth=2.5, marker='o')

plt.xlabel('Fiscal Years')
plt.ylabel('Number of Patients')
plt.title('Gender')
plt.legend()
plt.xticks(years, years) # (x value, xtricks)
plt.margins(0.2)
plt.grid(True)

plt.show()

# close file gender.txt
file.close()
