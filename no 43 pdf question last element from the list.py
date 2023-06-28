##Q43. Make a function given a list [‘a’, 1, ‘2’, 5, ‘b’, ‘q’]. Print the last ‘N’ elements of the given list. ‘N’ is accepted from
##the user.
##Sample Input:
##1
##Sample Output:
##q
##Sample Input:
##3
##Sample Output:
##5
##b
def list1(n,list):
    i=1
    while i<len(list):
        a=list[-i:]
        if i==n:
            break
        i=i+1
    print(a)
n=int(input("enter number"))
list=["a", 1, "2", 5, "b", "q"]
list1(n,list)
