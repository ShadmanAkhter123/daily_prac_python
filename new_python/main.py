##neon number

n= int(input("Enter a number: "))

s= n*n

c=s
r=0

while c>0:
    b=c%10
    r= b+r
    c=c//10

if r==n:
    print("Neon number")
else:
    print("not a neon number")









