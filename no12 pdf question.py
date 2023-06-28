#Q12.Numbers ending with zeros are boring.
#They might be fun in your world, but not here.
#Get rid of them. Only the ending ones.
#1450 -> 145
#960000 -> 96
#31050 -> 105
#-1050 -> -105
def num(ending):
    i=0
    a=str(ending)
    b=list(a)
    i=0
    while i<len(b):
        if b[-1]=='0':
            b.remove(b[-1])
        i=i+1
    print(b)
    

    
a=int(input("enter num"))
num(a)
            


        
