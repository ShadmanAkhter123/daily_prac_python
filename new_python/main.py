##Strong number

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

n= int(input("Enter the number: "))
c=n
r=0

while c>0:
    b=c%10
    r= r+factorial(b)
    c= c//10

if r==n:
    print("Its a strong number")
else:
    print("it's not a strong number")









