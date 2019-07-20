# 1~N까지 합과 평균
def calSumAverage(firstnumber,lastnumber):   
    sum=0
    mylist = []

    for i in range(int(firstnumber),int(lastnumber)+1):
        mylist.append(i)
    #print(mylist)

    for num in mylist:
        sum = sum+num
    print(sum)

    average = sum/len(mylist)
    print (average)

a=input("input First Number: ")
b=input("input Second Number: ")

calSumAverage(a,b)
