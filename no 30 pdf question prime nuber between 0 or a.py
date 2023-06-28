#30. Write a function that prints all the prime numbers between 0 and limit where limit is a
#parameter.
def prime(a):
    i=0
    b=[]
    while (i<=a):
        j=1
        count=0
        while j<=i:
            if (i%j==0):
                count+=1
            j=j+1
        if (count==2):
            b.append(i)
        i=i+1
    print(b)
    print(len(b))
    k=0
    while k<len(b):
        c=b[1]
        k=k+1
    print(c)
       
a=int(input("enter number"))
prime(a)
