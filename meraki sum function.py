#Q2. You have to print the sum of the elements of the given list
#by using the sum function.
a = [1, 2, 3, 4, 5]
def sum1(a):
    i=0
    sum=0
    while i<len(a):
        sum=sum+a[i]
        i=i+1
    print(sum)   

sum1(a)
#a = [1, 2, 3, 4, 5]
#print(sum(a))
