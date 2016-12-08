import pygal
from pygal.style import Style

def gender():
    """Graph Gender"""
    # the data
    # open file gender.txt
    file = open('graph/gender.txt', 'r')
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
    line_chart.render_to_file('graph/img-svg/gender_line.svg')

    # close file type.txt
    file.close()
gender()

def ages():
    """The graph shows result about ages between 2555-2558 Percent_Vers"""
    gauge = pygal.SolidGauge(inner_radius=0.70)
    gauge.title = "กลุ่มอายุการใช้ยาเสพติด ปี 2555-2558"
    percent_formatter = lambda x: '{:.10g}%'.format(x)
    gauge.value_formatter = percent_formatter
    gauge.add('0-14 ปี', [{'value': 2.63, 'max_value': 100}])
    gauge.add('15-24 ปี', [{'value': 36.47, 'max_value': 100}])
    gauge.add('25-54 ปี', [{'value': 58.02, 'max_value': 100}])
    gauge.add('55+ ปี', [{'value': 2.88, 'max_value': 100}])
    gauge.render_to_file('graph/img-svg/age_guage.svg')

    """The graph shows result about ages between 2555-2558"""
    custom_style = Style(
    colors=('#2E64FE', '#E8537A', '#FFFF00', '#3ADF00'))
    bar_chart = pygal.Bar(style=custom_style, x_title="ปี", y_title="จำนวนผู้ป่วย")
    bar_chart.title = "กลุ่มอายุการใช้ยาเสพติด ปี 2555-2558"
    bar_chart.x_labels = "ปี 2555", "ปี 2556", "ปี 2557", "ปี 2558"
    bar_chart.add('0-14 ปี', [256, 131, 144, 145])
    bar_chart.add('15-24 ปี', [3543, 2864, 2478, 1852])
    bar_chart.add('25-54 ปี', [5637, 4702, 4280, 3381])
    bar_chart.add('55+ ปี', [279, 263, 269, 288])
    bar_chart.render_to_file('graph/img-svg/ages_linebar.svg')
ages()

def types():
    """Graph total type of drugs in years 2555-2558"""
    # the data
    # open file type.txt
    file = open('graph/type.txt', 'r')
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
    pie_chart.render_to_file("graph/img-svg/type_pie.svg")

    """Graph type of drugs"""
    years = []
    y2555 = []
    y2556 = []
    y2557 = []
    y2558 = []
    for d in data:
        years.append(d.pop(0))
    y2555 = [int(i) for i in data[0]]
    y2556 = [int(i) for i in data[1]]
    y2557 = [int(i) for i in data[2]]
    y2558 = [int(i) for i in data[3]]

    # plot graph
    bar_chart = pygal.HorizontalBar(fill=True, interpolate='cubic', x_title="จำนวนผู้ป่วย", y_title="ประเภทของยาเสพติด")
    bar_chart.title = "การเพิ่มขึ้น/ลดลงของจำนวนผู้ป่วยตามประเภทยาเสพติด ปี 2555-2558"
    bar_chart.x_labels = ['เฮโรอีน', 'ฝิ่น', 'กัญชา', 'กระท่อม', 'ยากล่อมประสาท', 'ยาบ้า', 'ยานอนหลับ', 'สุรา', 'ยานอนหลับ','บุหรี่','ยาไอซ์', 'อื่นๆ']
    bar_chart.add(years[0], y2555)
    bar_chart.add(years[1], y2556)
    bar_chart.add(years[2], y2557)
    bar_chart.add(years[3], y2558)
    bar_chart.render_to_file("graph/img-svg/type_bar.svg")

    # close file type.txt
    file.close()
types()

def why():
    """Graph whyusepie"""
    why = []
    data = []
    #import data
    file = open("graph/why.txt","r")
    for line in file:
        why.append(line.strip('\n').split())
    for i in why:
        data.append(int(i[0]) + int(i[1]) + int(i[2]) + int(i[3]))

    pie_chart = pygal.Pie(inner_radius=.5)
    # Plot pie_chart
    pie_chart.title = 'สาเหตุการใช้ยาตั้งแต่ปี 2555-2558'
    #using data 
    pie_chart.add('ทดลองใช้เอง', data[0])
    pie_chart.add('เพื่อนชวน', data[1])
    pie_chart.add('สนุกสนาน', data[2])
    pie_chart.add('เจ็บป่วย', data[3])
    pie_chart.add('มีปัญหา', data[4])
    pie_chart.add('ช่วยงานอาชีพ', data[5])
    pie_chart.add('มีอาการอย่างเสพ', data[6])
    pie_chart.add('อื่นๆ', (data[7] + data[8]))
    pie_chart.render_to_file('graph/img-svg/whyusepie.svg')

    
    """Graph whyusebar"""
    line_chart = pygal.Bar(x_title="ปี", y_title="จำนวนผู้ป่วย")
    why = []
    data = []
    #import data
    file = open("graph/why.txt","r")
    for line in file:
        why.append(line.strip('\n').split())
    for i in why:
        data.append(int(i[0]))
        data.append(int(i[1]))
        data.append(int(i[2]))
        data.append(int(i[3]))

    # Plot line_chart
    line_chart.title = 'สัดส่วนของสาเหตุการใช้ยาตั้งแต่ปี 2555-2558'
    line_chart.x_labels = map(str, range(2555, 2559))
    #using data 
    line_chart.add('ทดลองใช้เอง', [data[0], data[1], data[2], data[3]])
    line_chart.add('เพื่อนชวน', [data[4], data[5], data[6], data[7]])
    line_chart.add('สนุกสนาน', [data[8], data[9], data[10], data[11]])
    line_chart.add('เจ็บป่วย', [data[12], data[13], data[14], data[15]])
    line_chart.add('มีปัญหา', [data[16], data[17], data[18], data[19]])
    line_chart.add('ช่วยงานอาชีพ', [data[20], data[21], data[22], data[23]])
    line_chart.add('มีอาการอย่างเสพ', [data[24], data[25], data[26], data[27]])
    line_chart.add('อื่นๆ', [data[28] + data[32], data[29] + data[33], data[30] + data[34], data[31] + data[35]])
    line_chart.render_to_file('graph/img-svg/whyusebar.svg')
    # close file why.txt
    file.close()
why()

def heal():
    #import data
    year = []
    label = []
    hardf = []
    money = []
    arrest = []
    future = []
    force = []
    heatlh = []
    other = []
    data = []
    file = open("graph/heal.txt","r")
    for line in file:
        data.append(line.strip('\n').split())
    # split data to target list
    year.append(data[0])
    label.append(data[1])
    hardf.append(data[2])
    money.append(data[3])
    arrest.append(data[4])
    future.append(data[5])
    force.append(data[6])
    heatlh.append(data[7])
    other.append(data[8])

    """The graph shows the reason that use """  
    pie_chart = pygal.Pie(inner_radius=.45)
    pie_chart.title = "สาเหตุการเข้ารับการรักษา ตั้งแต่ปี 2555-2558"
    pie_chart.add(label[0][0], int(hardf[0][0]) + int(hardf[0][1]) + int(hardf[0][2]) + int(hardf[0][3]))
    pie_chart.add(label[0][1], int(money[0][0]) + int(money[0][1]) + int(money[0][2]) + int(money[0][3]))
    pie_chart.add(label[0][2], int(arrest[0][0]) + int(arrest[0][1]) + int(arrest[0][2]) + int(arrest[0][3]))
    pie_chart.add(label[0][3], int(future[0][0]) + int(future[0][1]) + int(future[0][2]) + int(future[0][3]))
    pie_chart.add(label[0][4], int(force[0][0]) + int(force[0][1]) + int(force[0][2]) + int(force[0][3]))
    pie_chart.add(label[0][5], int(heatlh[0][0]) + int(heatlh[0][1]) + int(heatlh[0][2]) + int(heatlh[0][3]))
    pie_chart.add(label[0][6], int(other[0][0]) + int(other[0][1]) + int(other[0][2]) + int(other[0][3]))
    pie_chart.render_to_file('graph/img-svg/heal_pie.svg')

    """The graph shows the reason that use per years"""
    bar_chart = pygal.Bar(x_title="เหตุผล", y_title="จำนวนผู้ป่วย")
    bar_chart.title = "สาเหตุการเข้ารับการรักษา"
    bar_chart.x_labels = label[0]
    bar_chart.add(year[0][0], [int(hardf[0][0]), int(money[0][0]), int(arrest[0][0]), int(future[0][0]), int(force[0][0]), int(heatlh[0][0]), int(other[0][0])])
    bar_chart.add(year[0][1], [int(hardf[0][1]), int(money[0][1]), int(arrest[0][1]), int(future[0][1]), int(force[0][1]), int(heatlh[0][1]), int(other[0][1])])
    bar_chart.add(year[0][2], [int(hardf[0][2]), int(money[0][2]), int(arrest[0][2]), int(future[0][2]), int(force[0][2]), int(heatlh[0][2]), int(other[0][2])])
    bar_chart.add(year[0][3], [int(hardf[0][3]), int(money[0][3]), int(arrest[0][3]), int(future[0][3]), int(force[0][3]), int(heatlh[0][3]), int(other[0][3])])
    bar_chart.render_to_file('graph/img-svg/heal_histo.svg')
heal()
