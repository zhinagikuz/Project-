"""
    Prototype of project
    Collaborators:Jirawan  Chuapradit     59070027
                  Thanadon Lertrumporn    59070065
                  Benjawan simpattanawong 59070093
                  Isara    Phoeon         59070193
"""
import matpoltlib as mat
import numpy as py
def graph_1():
    """
        This function use to calculate population of people with drugs split it with
         type of sex then show it on linear graph
    """

def graph_2():
    """
        This function use to calculate population of people with drugs split it with age
        then show it on pie chart 
    """

def graph_3():
    """
        This function use to calculate population of people with drugs split it with type of drugs
        then show it on bar graph
    """

def graph_4():
    """
        This function use to calculate population of people with drugs split it with reasons that take drugs
        then show it on pie chart
    """

def graph_5():
    """
        This function use to calculate population of people with drugs split it with cause admitted
        then show it on pie chart
    """
pie chartcode:
import matplotlib.pyplot as plt

# The slices will be ordered and plotted counter-clockwise.
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')