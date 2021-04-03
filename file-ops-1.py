with open('workfile.txt','w+') as f:
    f.write("hello")
    f.seek(0)
    read_data = f.read()
    print(read_data)
    print(f.closed)
    
f.close
print(f.closed)