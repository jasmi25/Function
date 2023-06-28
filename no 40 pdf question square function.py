#Q40. Write a function For example, if we give 9119 the function should return 811181, as the square of 9
#is 81 and square of 1 is 1.
def square(a):
    i=0
    sum=""
    while i<len(a):
        b=int(a[i])**2
        sum=sum+str(b)
        i=i+1
    return sum
a=input("enter number")
print(square(a))
