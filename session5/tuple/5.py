tuple1 = []
woof = int(input("Enter the number of records"))


for i in range(woof):
    print("Enter the record of",i+1,"student")
    meow = input("Enter the student's name")
    meow1 = input("Enter higher education")
    meow2 = input("Enter primary skill")
    meow3 = input("Enter year of graduation")

    tuple1.append((meow,meow1,meow2,meow3))
print(tuple1)

woof1 = input("Enter higher education")
woof2 = input("Enter primary skill")
woof3 = input("Enter year of graduation")
for i in tuple1:
  if i[1]==woof1 and i[2]==woof2 and i[3]==woof3:
         print(i)
  else:
      print("no meow")
    
    
  

