#Q42. Find the sum of number digits in List
##The original list is : [12, 67, 98, 34]
##List Integer Summation : [3, 13, 17, 7]
##Explanation: 1+2 = 3, 6+7=13, 9+8=17, 3+4=7
##The original list is : [15, 81, 11, 234]
#list=[12, 67, 98, 34]
def sum_num_of_digit(list):
    a=[]
    for i in list:
        sum=0
        for j in str(i):
            sum+=int(j)
        a.append(sum)
    print(a)
sum_num_of_digit([12, 67, 98, 34])
