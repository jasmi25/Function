##Q44.Bonus - Given the same list, print the last ‘N’ elements in reverse order.
##Sample Input:
##2
##Sample Output:
##q
##b
##Sample Input:
##3
##Sample Output:
##q
##b
##5
def rev(n):
    list=["a", 1, "2", 5, "b", "q"]
    i=1
    while i<len(list):
        a=list[-n:]
        a.reverse()
        i=i+1
    print(a)
n=int(input("enter last element"))
print(rev(n))
