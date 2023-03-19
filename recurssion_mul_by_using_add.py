
def sum_add(a,b):
    if a == 1:
        return b
    return sum_add(a-1,b) +b


print(sum_add(10,3))
