"""Graph total type of drugs in years 2555-2558"""
import pygal

# the data
# open file type.txt
file = open('type.txt', 'r')
data = []
years = []
heloin = []
opium = []
weed = []
kratom = []
sedative = []
amphetamine = []
narcotic = []
alcohol = []
volatile = []
cigarette = []
ice = []
other = []
for d in file:
    data.append(d.strip('\n').split())
for i in data:
    years.append(int(i[0]))
    heloin.append(int(i[1]))
    opium.append(int(i[2]))
    weed.append(int(i[3]))
    kratom.append(int(i[4]))
    sedative.append(int(i[5]))
    amphetamine.append(int(i[6]))
    narcotic.append(int(i[7]))
    alcohol.append(int(i[8]))
    volatile.append(int(i[9]))
    cigarette.append(int(i[10]))
    ice.append(int(i[11]))
    other.append(int(i[12]))

# plot graph
pie_chart = pygal.Pie(inner_radius=0.6)
pie_chart.title = "Total type of drugs in 2555-2558"
pie_chart.add('Helion', sum(heloin))
pie_chart.add('Opium', sum(opium))
pie_chart.add('Weed', sum(weed))
pie_chart.add('kratom', sum(kratom))
pie_chart.add('Sedative', sum(sedative))
pie_chart.add('Amphetamine', sum(amphetamine))
pie_chart.add('Narcotic', sum(narcotic))
pie_chart.add('Alcohol', sum(alcohol))
pie_chart.add('Volatile', sum(volatile))
pie_chart.add('Cigarette', sum(cigarette))
pie_chart.add('Ice', sum(ice))
pie_chart.add('Other', sum(other))
pie_chart.render_to_file("img-svg/type_pie.svg")

# close file type.txt
file.close()
