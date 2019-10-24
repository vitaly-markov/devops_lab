def mydict (keys, values):
 while len(keys) > len(values):
  values.append('None')
 e = dict(zip(keys, values))
 print(e)
 return e




