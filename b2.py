def breakdown(value):
    m=() # Don't use a tuple here. Since you're adding to it, use a list
    d=[1000,500,100,50,20,10,1]
    for amount in d:
        num=int(value/amount)
        m+=(amount,)*num
        value-=(amount*num)
        print("{} * {} = {} {}".format(amount,num,num*amount,m))
        #                                                    ^
        # You should print the remaining or dispensed amount at the end. Not m
