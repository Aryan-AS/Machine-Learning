# test = {"CampusX" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}
# # print(list(test)), only keys are extracted when you convert a dic to list
# sum = []
# for i in test.values():
#     for j in i:
#      if j not in sum:
#       sum.append(j)
      
      
# print(sum)

# write your code here
test_dict = {"CampusX" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]}
# for i in test_dict:
#     print(i) loop iterates over keys only
for i in test_dict:
    print(test_dict[i])
      
