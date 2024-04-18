list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]
list2 = 0
set1 = 0
tuple1=0
for i in list1:
    if type(i)==set:
        set1 = set1 + 1
        print("meow")
    if type(i)==list:
        list2 = list2+1
    if type(i)==tuple:
        tuple1=tuple1+1
print("list", list2)
print("set", set1)
print("tuple",tuple1)