from zipfile import *
f = ZipFile("C:/Users/a/Desktop/All_Files.zip","w",ZIP_DEFLATED)
f.write('C:/Users/a/Desktop/pqr.txt')
f.write('C:/Users/a/Desktop/xyz.txt')
f.close()
print("Zip File Successfully Created")

from zipfile import *
f = ZipFile("C:/Users/a/Desktop/All_Files1.zip","w",ZIP_DEFLATED)
names = f.namelist()
#print(names)
for name in names:
    print("file name :",name)
    print("the content of file is : ")
    f1 = open(name,'r')
    print(f1.read())
    print()