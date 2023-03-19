def len_of_str(str1):
    if str1 == "":
        return 0
    return 1 + len_of_str(str1[1:])


print(len_of_str("Hari"))
