print("Enter the following words in accordance with your needs")
print("A for cm to ft calculation")
print("B for km to miles calculation")
print("C for USD to INR calculation")
print("D for exit")
a = str(input("Enter the word here:"))
if(a=="A"):
    a = int(input("Enter the cm value"))
    a = a*0.0328
    print("The value in feet would be",a)

if(a=="B"):
    a = int(input("Enter the km value"))
    a = a*0.62137119
    print("The value for miles would be",a)

if(a=="C"):
    a = int(input("Enter the USD value here"))
    a = a*83.37
    print("The value in INR would be",a)
if(a=="D"):
    print("Thanks for using our calculator")



