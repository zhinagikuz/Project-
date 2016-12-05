"""The graph shows result about ages between 2555-2558 Percent_Vers"""
import pygal
<<<<<<< HEAD
gauge = pygal.SolidGauge(inner_radius=0.70)
gauge.title = "กลุ่มอายุการใช้ยาเสพติด ปี 2555-2558"
percent_formatter = lambda x: '{:.10g}%'.format(x)
gauge.value_formatter = percent_formatter
gauge.add('0-14 ปี', [{'value': 2.63, 'max_value': 100}])
gauge.add('15-24 ปี', [{'value': 36.47, 'max_value': 100}])
gauge.add('25-54 ปี', [{'value': 58.02, 'max_value': 100}])
gauge.add('55+ ปี', [{'value': 2.88, 'max_value': 100}])

gauge.render_to_file('age_guage.svg')
=======
from pygal.style import Style
custom_style = Style(
colors=('#2E64FE', '#E8537A', '#FFFF00', '#3ADF00'))
bar_chart = pygal.Bar(style=custom_style, x_title="Years", y_title="Number of Patients")
bar_chart.title = "กลุ่มอายุการใช้ยาเสพติด ปี 2555-2558"
bar_chart.x_labels = "ปี 2555", "ปี 2556", "ปี 2557", "ปี 2558"
bar_chart.add('0-14 ปี', [256, 131, 144, 145])
bar_chart.add('15-24 ปี', [3543, 2864, 2478, 1852])
bar_chart.add('25-54 ปี', [5637, 4702, 4280, 3381])
bar_chart.add('55+ ปี', [279, 263, 269, 288])
bar_chart.render_to_file('ages_linebar.svg')
>>>>>>> refs/remotes/origin/jugjig
