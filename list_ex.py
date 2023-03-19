my_list = [1, 2, 1, 3, 333, 333, "test", 33, 10, 11, 1, 15, 123, 1234, 113, 123, "test", "test2", "a", "test", 11, 333, 1, 22, 2]
print("first", my_list)
exp=set(my_list)
length = len(my_list)
j = 1
k=1
for i in my_list:
    j=k
    while i in my_list[j:]:
        my_list[j:].remove(i)
        j+=1
    k+=1
print("out",my_list,"len",len(my_list))      
print("setout",exp,"len",len(exp))


