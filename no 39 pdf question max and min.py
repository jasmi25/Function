##Q39. Your task is to make two functions, max and min (maximum and minimum in PHP and
##Python, maxi and mini in Julia) that take a(n) array/vector of integers list as input and outputs,
##respectively, the largest and lowest number in that array/vector.
###Examples:-
##maximun([4,6,2,1,9,63,-134,566]) returns 566
##minimun([-52, 56, 30, 29, -54, 0, -110]) returns -110
##maximun([5]) returns 5.
##minimun([42, 54, 65, 87, 0]) returns 0.
def list(arr):
    i=0
    max=arr[0]
    while i<len(arr):
        if arr[i]>max:
            max=arr[i]
        i=i+1
    return max
a=([4,6,2,1,9,63,-134,566])
print(list(a))
def list(arr):
    i=0
    min=arr[0]
    while i<len(arr):
        if arr[i]<min:
            min=arr[i]
        i=i+1
    return min
a=([-52, 56, 30, 29, -54, 0, -110])
print(list(a))
        
