import csv
with open ('C:/Users/a/Desktop/stud.csv',"w")as f:
    w = csv.writer(f)
    w.writerow(['Roll No','Name','Percentage','Address'])
    n = int(input("Enter Number of Student : "))
    for i in range(n):
        Rollno = input("Enter Student Roll No : ")
        Name = input("Enter Student Name : ")
        Percentage = input("Enter Student Percentage : ")
        Address =  input("Enter Student Address : ")
        w.writerow([Rollno,Name,Percentage,Address])
        print("Data Written Successfully")

#read csv data
import csv
f = open ('C:/Users/a/Desktop/stud.csv',"r")
r = csv.reader(f)
data = list(r)
print(data)

#print data
for line in data:
    for word in line:
        print(word,"\t",end="")
        print()
