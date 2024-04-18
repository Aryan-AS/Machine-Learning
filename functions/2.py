meow = "green-red-yellow-black-white"
def sortstring(meow):
 moo = []
 for i in sorted(meow.split("-")):
     moo.append(i)

 return "-".join(moo)
print(sortstring(meow))




