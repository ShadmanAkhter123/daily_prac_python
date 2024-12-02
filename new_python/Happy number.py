# happy number

n = int(input("Enter the number: "))

a= n

while(a==1)


    b= int(a/10)
    c= a%10

    a= b**2+c**2

print(f"{b}, {c}    {a}")