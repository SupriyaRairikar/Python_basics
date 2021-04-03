try:
    fd=open("newfile.txt",'w+')
    fd.write("hello try block-----")
except:
    print("could not open the file")
finally:
    print("hello this is finally block")
    fd.seek(0)
    read_data = fd.read()
    print(read_data)
    print(fd.closed)
    fd.close()
    print(fd.closed)
