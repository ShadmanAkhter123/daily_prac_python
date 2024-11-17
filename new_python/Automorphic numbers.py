##automorphic numbers


n= int(input("enter the number: "))

c = n
r=10
s=n*n
y=s
x= False

while y > 0:
    b= y%10
    a= s%r
    if a==n:
        x= True
        break
    y=y//10

    r= r*10


if x:
    print("automorphic number")
else:
    print("not a automorphic number")
