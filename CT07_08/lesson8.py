print("Hello from lesson 8")

number = ""
counter = -1
list1 = [3, 2, 1]
list2 = [6, 5, 5]
list3 = [9, 8, 7]

big_list = list1 + list2 + list3

for i in big_list:
    counter += 1
    big_list = number
    if number in big_list:
        big_list.pop(counter)
    



