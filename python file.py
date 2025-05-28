f=open("python programming.py","r")
data=f.read(4)
data1=f.readline()
print(data1)
print(type(data))
f.close()
f1=open("python programming.py","a")
p=f1.write("# this is a new line")
f1.close()
with open("python programming.py","r") as f:
    p=f.read()
   print(p)
    #with open("new file.txt","w") as y:
     #   y.write("#this is second line") 
     import os
     os.remove("new file.txt")