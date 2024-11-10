##Perfect number in python

n= int(input("Enter the number: "))

b=[]
a= 1
while a<=n/2:
    i= n%a
    if i==0:
        b.append(a)
    a+=1

for j in range(len(b)):
    b[j]+=b[j]

if b[j]==n:
    print("perfect number")
else:
    print("not a perfect number")

