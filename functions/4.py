list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even_list(list1):
    list2 = []
    for i in list1:
        if i%2==0:
            list2.append(i)
    return list2
print(even_list(list1))