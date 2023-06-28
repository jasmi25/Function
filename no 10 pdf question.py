#Q10.Create a function that takes 2 positive integers in form of a string as an input, and outputs the
#sum (also as a string):
#"4", "5" --> "9"
#"34", "5" --> "39"
#Notes:If either input is an empty string, consider it as zero.
def int_n(a,b):
    e=int(a)
    f=int(b)
    c=e+f
#    d=str(c)
    print(str(c))
x=input("enter 1st integers in form of a string")
y=input("enter 2nd integers in form of a string")
int_n(x,y)
n="34"
m="5"
int_n(n,m)
    
    
