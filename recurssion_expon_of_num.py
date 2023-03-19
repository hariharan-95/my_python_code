def find_expone_num(a, b):
    if b==1:
        return  a
    return find_expone_num(a,b-1)*a

print(find_expone_num(2,4))