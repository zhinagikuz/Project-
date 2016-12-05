"""The graph shows the reason that use """
import pygal
bar_chart = pygal.Bar(x_title="Reason", y_title="Number of Patients")
bar_chart.title = "สาเหตุการเข้ารับการรักษา"
bar_chart.x_labels = "หาซื้อยาก", "เงินไม่พอใช้", "กลัวถูกจับ", "เพื่ออนาคต", "ถูกบังคับ", "สุขภาพทรุดโทรม", "อื่นๆ"
bar_chart.add('2555', [{'value': 5280}, 2347, 750, 1, 7, 19, 1311])
bar_chart.add('2556', [{'value': 3871}, 2206, 511, 0, 3, 5, 1364])
bar_chart.add('2557', [{'value': 3223}, 1949, 538, 0, 1, 6, 1354])
bar_chart.add('2558', [{'value': 2663}, 1534, 310, 0, 5, 6, 1148])

bar_chart.render_to_file('heal.svg')