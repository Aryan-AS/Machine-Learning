
s = 'PyNaTive'

upper = ''
lower = ''

for i in s:
  if i.islower():
    lower = lower + i
  else:
    upper = upper + i

print(lower + upper)