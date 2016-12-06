import pygal

pie_chart = pygal.Pie(print_values=True, print_values_position='top')
why = []
data = []
#import data
file = open("555.txt","r")
for line in file:
    why.append(line.strip('\n').split())
for i in why:
    data.append(int(i[0]) + int(i[1]) + int(i[2]) + int(i[3]))

# Plot pie_chart
<<<<<<< HEAD
pie_chart.title = 'สัดส่วนของสาเหตุการใช้ยาตั้งแต่ปี 2555-2558 คิดเป็นเปอร์เซ็นต์'
=======
pie_chart.title = 'สัดส่วนของสาเหตุการใช้ยาตั้งแต่ปี 2555-2558'
>>>>>>> refs/remotes/origin/jugjig
#using data 
pie_chart.add('ทดลอง', data[0])
pie_chart.add('เพื่อนชวน', data[1])
pie_chart.add('สนุกสนาน', data[2])
pie_chart.add('เจ็บป่วย', data[3])
pie_chart.add('มีปัญหา', data[4])
pie_chart.add('ช่วยงานอาชีพ', data[5])
pie_chart.add('มีอาการอย่างเสพ', data[6])
pie_chart.add('อื่นๆ', (data[7] + data[8])
pie_chart.render_to_file('whyuse.svg')
