#Q2.Write a Python function to find the Max of three numbers.
def largest(x,y,z):
    if x>y and z<x:
        max=x
    elif y>z and x<y:
        max=y
    else:
        max=z
    print(max)
a=int(input('enter number'))    
b=int(input('enter number'))    
c=int(input('enter number'))
largest(a,b,c)
