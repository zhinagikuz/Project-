import pygal

line_chart = pygal.Bar(x_title="ปี", y_title="จำนวนผู้ป่วย")
why = []
data = []
#import data
file = open("555.txt","r")
for line in file:
    why.append(line.strip('\n').split())
for i in why:
    data.append(int(i[0]))
    data.append(int(i[1]))
    data.append(int(i[2]))
    data.append(int(i[3]))

# Plot pie_chart
line_chart.title = 'สัดส่วนของสาเหตุการใช้ยาตั้งแต่ปี 2555-2558'
line_chart.x_labels = map(str, range(2555, 2558))
#using data 
line_chart.add('ทดลอง', [data[0], data[1], data[2], data[3]])
line_chart.add('เพื่อนชวน', [data[4], data[5], data[6], data[7]])
line_chart.add('สนุกสนาน', [data[8], data[9], data[10], data[11]])
line_chart.add('เจ็บป่วย', [data[12], data[13], data[14], data[15]])
line_chart.add('มีปัญหา', [data[16], data[17], data[18], data[19]])
line_chart.add('ช่วยงานอาชีพ', [data[20], data[21], data[22], data[23]])
line_chart.add('มีอาการอย่างเสพ', [data[24], data[25], data[26], data[27]])
line_chart.add('อื่นๆ', [data[28] + data[32], data[29] + data[33], data[30] + data[34], data[31] + data[35]])
line_chart.render_to_file('img-svg/whyusebar.svg')
