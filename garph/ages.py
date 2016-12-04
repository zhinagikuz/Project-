"""The graph shows result about ages between 2555-2558"""
import pygal
#import data age.txt
from pygal.style import Style
custom_style = Style(colors=('#2E64FE', '#E8537A', '#FFFF00', '#3ADF00'))
bar_chart = pygal.Bar(style=custom_style)
bar_chart.title = "กลุ่มอายุการใช้ยาเสพติด ปี 2555-2558"
bar_chart.x_labels = "ปี 2555", "ปี 2556", "ปี 2557", "ปี 2558"
bar_chart.add('0-14 ปี', [256, 131, 144, 145])
bar_chart.add('15-24 ปี', [3543, 2864, 2478, 1852])
bar_chart.add('25-54 ปี', [5637, 4702, 4280, 3381])
bar_chart.add('55+ ปี', [279, 263, 269, 288])
bar_chart.render_to_file('ages2555.svg')
