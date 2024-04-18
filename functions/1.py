def meow(list1):
    sum = []
    for i in list1:
        if i not in sum:
            sum.append(i)

    return sum

list1 = [1,2,3,3,3,3,4,5]
print(meow(list1))