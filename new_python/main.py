##Armstrong number in python

n= int(input("input a number: "))

c=n
d=0

while c>0:
    b=int(c%10)
    d= d+b*b*b
    c = int(c/10)

if d==n:
    print("armstrong number")
else:
    print("not armstrong")






