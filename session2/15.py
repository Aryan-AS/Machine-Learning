# Write code here
print("Enter both Rectangel points coordinates <x y>")

l1_x, l1_y = list(map(int, input('Enter L1 coordinate value  (Two value space seperated):').split()))
r1_x, r1_y = list(map(int, input('Enter r1 coordinate value,(Two value space seperated):').split()))

l2_x, l2_y = list(map(int, input('Enter L2 coordinate value,(Two value space seperated):').split()))
r2_x, r2_y = list(map(int, input('Enter r2 coordinate value,(Two value space seperated):').split()))

# if rectangle has area 0, no overlap
if l1_x == r1_x or l1_y == r1_y or r2_x == l2_x or l2_y == r2_y:
  print("Don't Overlap")
  
# If one rectangle is on left side of other
elif l1_x > r2_x or l2_x > r1_x:
  print("Don't Overlap")

# If one rectangle is above other
elif r1_y > l2_y or r2_y > l1_y:
  print("Don't Overlap")
else:
  print("Overlap")