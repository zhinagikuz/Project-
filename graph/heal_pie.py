"""The graph shows the reason that use """
import pygal
pie_chart = pygal.Pie(print_values=True, print_values_position='top')
pie_chart.title = "สาเหตุการเข้ารับการรักษา ตั้งแต่ปี 2555-2558"
pie_chart.add("หาซื้อยาก", 15037)
pie_chart.add("เงินไม่พอใช้", 8036)
pie_chart.add("กลัวถูกจับ", 2109)
pie_chart.add("เพื่ออนาคต", 1)
pie_chart.add("ถูกบังคับ", 16)
pie_chart.add("สุขภาพทรุดโทรม", 36)
pie_chart.add("อื่นๆ", 5177)

pie_chart.render_to_file('img-svg/heal_pie.svg')
