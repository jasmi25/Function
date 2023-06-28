#list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
#list.reverse()
#print(list)
def reverse(list):
    n=0-len(list)
    i=-1
    a=[]
    while i>=n:
        c=list[i]
        a.append(c)
        i=i-1
    print(a)
reverse(["Z", "A", "A", "B", "E", "M", "A", "R", "D"])
   
