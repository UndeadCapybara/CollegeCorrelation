import copy
import math

#Reads the PomonaData File and funnels the data into the x, y, and z vectors
xdata  =[]
ydata = []
zdata = []

f = open("PomonaData.txt")
data = f.readlines()
f.close()
