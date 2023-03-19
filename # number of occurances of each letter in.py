# number of occurances of each letter in a string, print in dictionary form (key, value pair)
str1 = "Hello world hhhhowwwwwwwwwww are youuuuu"
count=0
d1={}
for i in str1:
    if i in d1:
        d1[i]+=1
    else:
        d1[i]=1
print(d1)

