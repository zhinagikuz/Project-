"""Graph Gender"""
import pygal
from pygal.style import DarkStyle

# the data
# open file gender.txt
file = open('gender.txt', 'r')
data = []
years = []
male = []
female = []
for d in file:
    data.append(d.strip('\n').split())
for d in data:
    years.append(d[0])
    male.append(int(d[1]))
    female.append(int(d[2]))
# plot graph
line_chart = pygal.Line(fill=True, interpolate='cubic', x_title="ปี", y_title="จำนวนผู้ป่วย", stroke_style={"width":3})
line_chart.title = 'เพศ'
line_chart.x_labels = years
line_chart.add('ชาย', male)

line_chart.add('หญิง', female)
line_chart.render_to_file('img-svg/gender_line.svg')

# close file type.txt
file.close()
