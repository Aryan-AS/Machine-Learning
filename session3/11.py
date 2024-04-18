# Code here

inp = 'Data science Mentorship Program'

res = ''

for i in inp.split():
  res = res + i[0].upper()

print(res)