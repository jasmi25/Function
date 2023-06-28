#Q9.Write a Python program to generate and print a list of first and last 5 elements where
#the values are square of numbers between 1 and 30 (both included).
#Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).
def square(list1,list2):
    i=0
    emtl=[]
    emt2=[]
    while i<len(list1):
        c=list1[i]*list1[i]
        d=list2[i]*list2[i]
        emtl.append(c)
        emt2.append(d)
        i=i+1
    print(emtl,emt2)
square([1,2,3,4,5],[26,27,28,29,30])
        
    
    
