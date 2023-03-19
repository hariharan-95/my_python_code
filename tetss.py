no_of_frnds = int(input())
list_1=[]
for i in range(no_of_frnds):
    tmp = input()
    list_1.append(tmp)
no_of_time_ball_passed = int(input())
starting_positoin = [input() for i in range(2)]
print(list_1,no_of_frnds,no_of_time_ball_passed,starting_positoin)
print(starting_positoin[0])