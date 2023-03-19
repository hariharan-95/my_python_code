def quick_sort(list1):
    if len(list1)<=1:
        return list1

    center=list1[len(list1)//2]
    left=[x for x in list1 if x < center]
    middle=[x for x in list1 if x == center]
    right=[x for x in list1 if x > center]

    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([8,1,7,2,9,5,3,7]))