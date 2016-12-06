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
pie_chart.title = "ผลรวมแต่ละประเภทยาเสพติดที่เสพ ปี 2555-2558"
pie_chart.add('เฮโรอีน', sum(heloin))
pie_chart.add('ฝิ่น', sum(opium))
pie_chart.add('กัญชา', sum(weed))
pie_chart.add('กระท่อม', sum(kratom))
pie_chart.add('ยากล่อมประสาท', sum(sedative))
pie_chart.add('ยาบ้า', sum(amphetamine))
pie_chart.add('ยานอนหลับ', sum(narcotic))
pie_chart.add('สุรา', sum(alcohol))
pie_chart.add('สาระเหย', sum(volatile))
pie_chart.add('บุหรี่', sum(cigarette))
pie_chart.add('ยาไอซ์', sum(ice))
pie_chart.add('อื่นๆ', sum(other))
pie_chart.render_to_file("img-svg/type_pie.svg")

# close file type.txt
file.close()
