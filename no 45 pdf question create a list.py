##Q45. Draw a flowchart to Take 10 numbers as input and create a list of the numbers from the user and update
##each element of the list according to below rule
##If it is even, then multiply it by 100
##If it is odd, then multiply it by -1
##Sample Input:
##23
##42
##41
##1
##Sample Output:
##-23
##4200
##-41
##-1
a=int(input("enter number a"))
list=[]
i=0
while i<=a:
    b=input("enter number b")
    list.append(b)
    i=i+1
    j=0
    mul=1
    while j<int(len(list)):
        if list[j]%2==0:
            a=list[j]*100
        else:
            b=list[j]*-1
        j=j+1
    print(a)
    print(b)
print(list)
