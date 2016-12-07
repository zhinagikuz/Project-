"""Graph type of drugs"""
import pygal
from pygal.style import DarkStyle

# the data
# open file type.txt
file = open('type.txt', 'r')
data = []
years = []
y2555 = []
y2556 = []
y2557 = []
y2558 = []
for d in file:
    data.append(d.strip('\n').split())
for d in data:
    years.append(d.pop(0))
y2555 = [int(i) for i in data[0]]
y2556 = [int(i) for i in data[1]]
y2557 = [int(i) for i in data[2]]
y2558 = [int(i) for i in data[3]]

# plot graph
bar_chart = pygal.HorizontalBar(fill=True, interpolate='cubic', x_title="จำนวนผู้ป่วย", y_title="ประเภทของยาเสพติด")
bar_chart.title = "การเพ่ิมขึ้น/ลดลงของจำนวนผู้ป่วยตามประเภทยาเสพติด ปี2555-2558"
bar_chart.x_labels = ['เฮโรอีน', 'ฝิ่น', 'กัญชา', 'กระท่อม', 'ยากล่อมประสาท', 'ยาบ้า', 'ยานอนหลับ', 'สุรา', 'ยานอนหลับ','บุหรี่','ยาไอซ์', 'อื่นๆ']
bar_chart.add(years[0], y2555)
bar_chart.add(years[1], y2556)
bar_chart.add(years[2], y2557)
bar_chart.add(years[3], y2558)
bar_chart.render_to_file("img-svg/type_bar.svg")

# close file type.txt
file.close()
