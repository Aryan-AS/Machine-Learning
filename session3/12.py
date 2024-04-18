# a = str(input("Enter the first string"))
# b = str(input("Enter the second string"))
# mid = int(len(a)/2)
# print(mid)
# for i in range(1,len(a)):
#     print(i)
#     if i == mid:
#         print(a(i)+b)
#     else:
#         print("meow")
    # Code here

s1 = input('enter the 1st string')
s2 = input('enter the 2nd string')

print(s1[0:int(len(s1)/2)] + s2 + s1[int(len(s1)/2):])