# write your code here
test_list = ["CampusX", 10]
key_list = ["name", "id"]

n = len(test_list)

res = []

for i in range(0,n,2):
  res.append({key_list[0]: test_list[i],key_list[1]:test_list[i+1]})

print(res)