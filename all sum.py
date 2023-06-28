##2. Write a Python function to sum all the numbers in a list. Go to the editor
##Sample List : (8, 2, 3, 0, 7)
##Expected Output : 20
def sum(list):
   sum=0
   i=0
   while i<len(list):
       sum=sum+list[i]
       i=i+1
   print(sum)
sum((8, 2, 3, 0, 7))
def add(*b):
    result=0
    for i in b:
        result=result+i
    return result
print(add(1,2,3,4,5))
