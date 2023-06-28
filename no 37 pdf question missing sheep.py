# Consider an array/list of sheep where some sheep may be missing from their place. We
#need a function that counts the number of sheep present in the array (true means present).
def arr_l(sheep):
    count=0
    i=0
    while i<len(sheep):
        if sheep[i]=="True":
            count=count+1
        i=i+1
    if count==17:
        print("sheep present in the array",count)
    else:
        print("some sheep missing from their place")
arr_l([True, True, True, False,
True, True, True, True ,
True, False, True, False,
True, False, False, True ,
True, True, True, True ,
False, False, True, True]
)
        
