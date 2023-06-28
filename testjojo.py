#Q12.Numbers ending with zeros are boring.
#They might be fun in your world, but not here.
#Get rid of them. Only the ending ones.
#1450 -> 145
#960000 -> 96
#31050 -> 105
#-1050 -> -105
def num(a):
    b=str(a)
    c=b.split(" ,")
    print(c)
a=int(input("enter number"))
num(a)
 
