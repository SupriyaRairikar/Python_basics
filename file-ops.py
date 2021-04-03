fs = open("test.txt")  #open file for read write options
#read_data = fs.read()   #read entire data from a file
#print(read_data)
read_data = fs.read(4)  #read only 4 bytes
print(read_data)
read_data = fs.read()   #read entire data from a file
print(read_data)
fs.close


fd1 = open('about-iot.txt','w+')
fd1.write("IOT is awesome")
fd1.seek(0)
data = fd1.read()   #read entire data from a file
print(data)

fd1.close