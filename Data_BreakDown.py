import copy
import math

#Reads the PomonaData File and funnels the data into the x, y, and z vectors
xdata  =[]
ydata = []
zdata = []

f = open("PomonaData.txt")
data = f.readlines()
f.close()

for i in range(len(data)):
  xdata.append(float(datapoint[0]))
  ydata.append(float(datapoint[1]))
  zdata.append(float(datapoint[2]))

#find average of x values
xcopy = copy.deepcopy(xdata)
xquant = 0
xsum = 0
for i in xcopy:
  xquant+=1
  xsum+=i
xavg = xsum/xquant

#find the average of the y values
ycopy = copy.deepcopy(ydata)
yquant = 0
ysum = 0
for i in ycopy:
  yquant+=1
  ysum+=i
yavg = ysum/yquant
#find average of z values
zcopy = copy.deepcopy(zdata)
zquant = 0
zsum = 0
for i in zcopy:
  zquant+=1
  zsum+=i
zavg = zsum/zquant

#subtracting mean
for i in range(len(xcopy)):
  xcopy[i] = xcopy[i] - xavg
for i in range(len(ycopy)):
  ycopy[i] = ycopy[i] - yavg
for i in range(len(zcopy)):
  zcopy[i] = zcopy[i] - zavg

dotproduct = 0
for i in range (len(xcopy)):
  dotproduct += xcopy[i] * zcopy[i]

xmag = 0
zmag = 0
for i in range(len(xcopy)):
  xmag += xcopy[i] * xcopy[i]
  zmag += zcopy[i] * zcopy[i]

xmag = math.sqrt(xmag)
zmag = math.sqrt(zmag)

correlationCo = dotproduct / (xmag * zmag)
print(correlationCo)
