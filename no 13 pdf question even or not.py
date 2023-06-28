#Q13.Write a function to check if a number is even or not.
def even(a):
    if a%2==0:
        print(a,"even")
    else:
        print(a,"not even")
b=int(input("enter number"))
even(b)
