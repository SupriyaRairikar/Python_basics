fd = open('sensordata.txt','w+')
fd.write("temp:20c humidity: 90")
fd.seek(0)
sensordata = fd.read()   #read entire data from a file
print(sensordata)
fd.close
