copyfile.py
file1=input("Enter First Filename : ")
file2=input("Enter Second Filename : ")
fn1 = open(file1, 'r')
fn2 = open(file2, 'w')
cont = fn1.readlines()
#type(cont)
for i in range(0, len(cont)):
 fn2.write(cont[i])
fn2.close()
print("Content of first file copied to second file ")
fn2 = open(file2, 'r')
cont1 = fn2.read()
print("Content of Second file :")
print(cont1)
fn1.close()
fn2.close()