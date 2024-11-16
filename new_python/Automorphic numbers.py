##automorphic numbers


n= int(input("enter the number: "))

c = n
r=0
s=n*n
y=s
x= []
while c >= 1:
    b = c % 10
    a= y%10

    x.append(a)
    y=int(y/10)
    c = c // 10
x.reverse()



print(x)