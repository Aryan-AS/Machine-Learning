list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1.insert([2][2],100) wrong because in a nested python creates a new list named [2], which doesnt exst  The list [2] has only one element, which is at index 0, not index 2. So, when you try to access index 2, Python raises an error because it's out of bounds for the list [2].
# list1[2][1].insert(3,600)
# list1[2][1].insert(3, 600): This attempts to call the insert() method on 400, which is an integer.

# The insert() method is a method of lists, not of integers. You can't call insert() on an integer. It's designed to be used with lists.

# Therefore, when you try to call insert() on 400, Python raises an AttributeError because integers do not have an insert() method.
list1[2][2].insert(3,7000)


print(list1)