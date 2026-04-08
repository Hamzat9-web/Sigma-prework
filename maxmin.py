def user_list():
    list = []
    num = ()
    print("Input a list numbers and type 'Stop' to complete the list")
    while num != "Stop":
        num = input("insert number: ")
        list.append(num)
    list.remove("Stop")
    list1 = []
    for i in list:
        list1.append(int(i))
    return list1
    print(list)


def maximum_num(list):
    max_num = list[0]
    for i in list:
        if i > max_num:
            max_num = i
    return max_num


def minmum_num(list):
    min_num = list[0]
    for i in list:
        if i < min_num:
            min_num = i
    return min_num


x = user_list()
minandmax = [minmum_num(x), maximum_num(x)]
print(minandmax)
