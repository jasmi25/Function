#Q14.Write a function to check if a number is prime or not.
def prime(a):
    count=0
    i=1
    while i<=a:
        if a%i==0:
            count+=1
        i=i=1
    if count==2:
        print("The number is a prime")
    else:
        print("The number is not a prime")
b=int(input("Enter a number"))
prime(b)
    
