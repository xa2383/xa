def make():
x=int(input("enter the value of x"))
for x in range(x):
if x%2==0:
yield x
gen=make()
print(list(gen))