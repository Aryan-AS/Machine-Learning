d = {"a":0,"e":0,"i":0,"o":0,"u":0}
with open("first.txt","r") as f:
 for j in f.read():
  for a in j.split():
   
   for i in a.lower():
    if i == "a":
     d["a"] += 1
      
    if i =="e":
      d["e"] += 1
    if i =="i":
       d["i"] += 1
     
    if i == "o":
       d["o"] += 1
     
    if i == "u":
       d["u"] += 1
       



print(d)
