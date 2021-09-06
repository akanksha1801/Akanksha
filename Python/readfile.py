f = open('C:/Users/a/Desktop/xyz.txt','r')
print('name:',f.name)
print('mode:',f.mode)
print('closed:',f.closed)
print('is readable : ',f.readable())
print('is writable : ',f.writable())
f.close()
print('closed:',f.closed)

f = open('C:/Users/a/Desktop/xyz.txt','w')
print('name:',f.name)
print('mode:',f.mode)
print('closed:',f.closed)
print('is readable : ',f.readable())
print('is writable : ',f.writable())
f.close()
print('closed:',f.closed)

#read first 10char
f = open('C:/Users/a/Desktop/pqr.txt','r')
data = f.read(10)
print(data)
f.close()

#read linebyline
f = open('C:/Users/a/Desktop/pqr.txt','r')
line1 = f.readline()
print(line1,end="")
line2 = f.readline()
print(line2,end="")
line3 = f.readline()
print(line3,end="")

#read all lines in list
f = open('C:/Users/a/Desktop/pqr.txt','r')
lines = f.readlines()
for line in lines:
    print(line,end="")

