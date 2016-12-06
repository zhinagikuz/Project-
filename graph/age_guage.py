"""The graph shows result about ages between 2555-2558 Percent_Vers"""
import pygal
gauge = pygal.SolidGauge(inner_radius=0.70)
gauge.title = "กลุ่มอายุการใช้ยาเสพติด ปี 2555-2558"
percent_formatter = lambda x: '{:.10g}%'.format(x)
gauge.value_formatter = percent_formatter
gauge.add('0-14 ปี', [{'value': 2.63, 'max_value': 100}])
gauge.add('15-24 ปี', [{'value': 36.47, 'max_value': 100}])
gauge.add('25-54 ปี', [{'value': 58.02, 'max_value': 100}])
gauge.add('55+ ปี', [{'value': 2.88, 'max_value': 100}])
gauge.render_to_file('img-svg/age_guage.svg')
