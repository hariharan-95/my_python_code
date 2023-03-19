import re

inp = int(input())
data = []
for _ in range(inp):
    data.append(input())
str1 = "\n".join(data)
patt = "\s[&]{2}\s"
patt2 = "\s[|]{2}\s"
sub_patt = " and "
sub_patt2 = " or "
tmp2 = re.sub(patt,sub_patt,str1)
print(tmp2)
tmp3= re.sub(patt2,sub_patt2,tmp2)
print(tmp3)

