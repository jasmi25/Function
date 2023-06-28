def num(b):
    i=1
    list=[]
    while i<=b:
        a=input("enetre number")
        list.append(a)
        j=0
        n=[]
        while j<len(list):
            c=int(list[j])
            if c%2==0:
                d=c*100
                n.append(d)
            else:
                e=c*-1
                n.append(e)
            j=j+1
        i=i+1
        print(list)
        print(n)
b=int(input("enter how many number you want")) 
num(b)
