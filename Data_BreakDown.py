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

#subtracting mean from each values in the vectors
for i in range(len(xcopy)):
  xcopy[i] = xcopy[i] - xavg
for i in range(len(ycopy)):
  ycopy[i] = ycopy[i] - yavg
for i in range(len(zcopy)):
  zcopy[i] = zcopy[i] - zavg

#dot product of x and z vector
dotproductxz = 0
for i in range (len(xcopy)):
  dotproductxz += xcopy[i] * zcopy[i]

#dot product of y and z vectors
dotproductyz = 0
for i in range(len(ycopy)):
  dotproductyz += ycopy[i] * zcopy[i]

#finds the magnitudes of each vector
xmag = 0
ymag=0
zmag = 0
for i in range(len(xcopy)):
  xmag += xcopy[i] * xcopy[i]
  ymag += ycopy[i] * ycopy[i] 
  zmag += zcopy[i] * zcopy[i]

xmag = math.sqrt(xmag)
ymag = math.sqrt(ymag)
zmag = math.sqrt(zmag)

#correlation coefficients
correlationCoxz = dotproductxz / (xmag * zmag)
correlationCoyz = dotproductyz / (ymag * zmag)

print(correlationCoxz)
print(correlationCoyz)
