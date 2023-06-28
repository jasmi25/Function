#Q8.Write a Python function that accepts a string and calculate the number of upper case letters and
#lower case letters. Go to the editor
#Sample String : 'The quick Brow Fox'
#No. of Uppercase characters : 3
#No. of Lower case Characters : 12
str= 'The quick Brow Fox'
def cha(str):
    i=0
    countu=0
    count=0
    while i<len(str):
        if str[i]>="A" and str[i]<="Z":
            countu+=1
        elif str[i]>="a" and str[i]<="z":
            count+=1
        i=i+1
    print(" No. of Uppercase characters : ", countu)
    print(" No. of Lower case Characters : ", count)
cha(str)
                
            
