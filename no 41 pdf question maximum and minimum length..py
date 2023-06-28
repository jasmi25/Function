#Q41. Write a Python program to find the list with maximum and minimum length.
#Original list:[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
#List with maximum length of lists:
#(3, [13, 15, 17])
#List with minimum length of lists:
#(1, [0])
a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
def lent(a):
    i=0
    max=[0]
    min=[0]
    n=len(a)
    while i<n:
        if(len(a[i])<len(min)):
            min=a[i]
        elif(len(a[i])>len(max)):
            max=a[i]
        i=i+1
    b=(len(min),min)
    d=(len(max),max)
    print(b)
    print(d)
lent([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])
