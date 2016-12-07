"""The graph shows the reason that use """
import pygal
pie_chart = pygal.Pie(inner_radius=.45)
pie_chart.title = "สาเหตุการเข้ารับการรักษา ตั้งแต่ปี 2555-2558"
pie_chart.add("เพื่ออนาคต", 15037)
pie_chart.add("ถูกบังคับ", 8036)
pie_chart.add("สุขภาพทรุดโทรม", 2109)
pie_chart.add("หาซื้อยาก", 1)
pie_chart.add("เงินไม่พอใช้", 16)
pie_chart.add("กลัวถูกจับ", 36)
pie_chart.add("อื่นๆ", 5177)
pie_chart.render_to_file('img-svg/heal_pie.svg')
