f = open('C:/Users/a/Desktop/nature.jpg','rb')
for i in f:
    print(i)

f = open('C:/Users/a/Desktop/nature.jpg','rb')
f1 = open('C:/Users/a/Desktop/nature1.jpg','wb')
bytes = f.read()
f1.write(bytes)

f = open('C:/Users/a/Desktop/nature.jpg','rb')
f1 = open('C:/Users/a/Desktop/nature3.jpg','wb')
for i in f:
    f1.write(i)

