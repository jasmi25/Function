#Q5. Use the min function and find the minimun value of the list.
list = [8, 6, 4, 8, 4, 50, 2, 7]
#print(min(list))
def min1(list):
    i=0
    min=list[0]
    while i<len(list):
        if list[i]<min:
            min=list[i]
        i=i+1
    return min
print(min1(list))
