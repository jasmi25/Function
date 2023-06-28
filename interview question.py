def num(list):
    i=0
    n_list=[]
    n=str(list)
    while i<len(n):
        if n[i] not in n_list:
            b=n[i]
            c=int(b)
            n_list.append(c)
        i=i+1
    print(n_list)
a=int(input("enter number"))
num(a)
    
 
