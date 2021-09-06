f = open('C:/Users/a/Desktop/pqr.txt','w')
f.write('Akanksha \n')
f.write('Rajendra \n')
f.write('Mali')
print('Data Written Successfully')
f.close()

#write list
f = open('C:/Users/a/Desktop/pqr.txt','w')
list = ['c\n','c++\n','Java\n','Python\n','Advanced Java\n','Javascript']
f.writelines(list)
print('List of Lines Written Successfully')
f.close()
