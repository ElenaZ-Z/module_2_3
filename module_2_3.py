my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
n = 0
my_list_index = my_list[n]
dlina = len(my_list)
while my_list_index >= 0 or n == dlina - 1:
    if my_list_index > 0:
        print(my_list_index)
    n = n + 1
    my_list_index = my_list[n]

