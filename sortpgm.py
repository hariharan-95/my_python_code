list1=[1,4,3,8,11,65,1,87,40,1243,61]
tmp=1
len_l=len(list1)
print("original",list1)
for i in range(0,len_l):
    for j in range(tmp,len_l):
        if list1[i] > list1[j]:
            print(list1[i],list1[j])
            list1[i],list1[j] = list1[j],list1[i]
            print("list",list1)
    tmp+=1
print(list1) v    