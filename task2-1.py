#Даны два произвольных списка. Удалите из первого списка элементы, присутствующие во втором.


my_list_1 = [2, 5, 8, 2, 12, 12, 4, 8, 4, 12, 3]
my_list_2 = [2, 7, 12, 3]


for member_in_list2 in my_list_2:
    i=0
    while i < my_list_1.count(member_in_list2):
        my_list_1.remove(member_in_list2)

print(my_list_1)


print(set(my_list_1))



