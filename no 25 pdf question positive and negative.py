#Q25. Given a list of numbers, write a Python program to count positive and negative numbers in a List using
#function.
#Example:
#list1 = [2, -7, 5, -64, -14]
#Output: pos = 2, neg = 3

def p_n(list):
    i=0
    p_count=0
    n_count=0
    while i<len(list):
        if list[i]>0:
            p_count+=1
        else:
            n_count+=1
        i=i+1
    print("number of positive",p_count)
    print("number of negative",n_count)
p_n([2, -7, 5, -64, -14])
