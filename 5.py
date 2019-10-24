moves = input()
x=0
y=0
for m in moves:
  if m == 'L':
   x = x - 1
  elif m == 'R':
   x = x + 1
  elif m == 'U':
   y = y + 1
  else:
   y = y - 1
if (x == 0) and (y == 0):
 print ("True")
else:
 print ("False")

