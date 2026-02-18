n=int(input("Enter the values:"))
a=0
b=1
i=0
print("Fibonacci series:")
while i<n:
    print(a,end="")
    c=a+b
    a=b
    b=c
    i+=1
    