""""
str1="192.168.39.108/27 "
list1=str1.split("/")
sub_range=int(list1[1])
range_of_sub=2**sub_range
tmp1=[]  ##[0,31,63,95,127,]
for i in range(0,255,32):
    tmp1.append(i)
    last_octent=108
    for i in len(tmp1):
        if int(last_octent) > tmp[i]:   
            if intt(last_octent) < tmp[i+1]:
                print("subnet is range ,tmp[i] to tmp[i+1]")
"""


def dis(price, discount):
    fnl_price = price - ((price*discount)/100)
    return fnl_price


assert dis(100, 75) == 25, "dail"
