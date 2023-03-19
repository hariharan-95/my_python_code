placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

d={}
for i in placement:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1

print(d)
ks = d.keys()
# initialize variable best_key_so_far to be the first key in d
min_value_1=list(ks)[0]
print(d.keys())
print(sorted(list(d.values())))
for k in ks:
    if d[k]<d[min_value_1]:
        d[min_value_1]=d[k]
        min_value=k
