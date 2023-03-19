str1 = "peter piper picked a peck of pickled peppers"
freq={}
for i in str1:
    if i not in str1:
        freq[i]=1
    else:
        freq[i]+=1