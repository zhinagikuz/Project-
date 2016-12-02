import pygal

pie_chart = pygal.Pie()
why = []
data = []
#import data
file = open("555.txt","r")
for line in file:
    why.append(line.strip('\n').split())
for i in why:
    data.append(int(i[0]) + int(i[1]) + int(i[2]) + int(i[3]))

# Plot pie_chart
pie_chart.title = 'สัดส่วนของสาเหตุการใช้ยาตั้งแต่ปี 2555-2558 (in %)'
#using data 
pie_chart.add('ทดลอง', data[0] / data[9])
pie_chart.add('เพื่อนชวน', data[1] / data[9])
pie_chart.add('สนุกสนาน', data[2] / data[9])
pie_chart.add('เจ็บป่วย', data[3] / data[9])
pie_chart.add('มีปัญหา', data[4] / data[9])
pie_chart.add('ช่วยงานอาชีพ', data[5] / data[9])
pie_chart.add('มีอาการอย่างเสพ', data[6] / data[9])
pie_chart.add('อื่นๆ', (data[7] + data[8]) / data[9])
pie_chart.render_to_file('whyuse.svg')
