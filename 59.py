list1 = ['Red', 'Green', 'Blue', 'Yellow', 'Black']

print('Positive Indexs in Ascending Order:')
print('Index \t List elements')
print('----- \t -------------')

for i in range(len(list1)):
  print(i, '\t', list1[i])
  
print('Positive Index in Descending Order:')
print('Index \t List elements')
print('----- \t -------------')

for i in range(len(list1)-1,-1,-1):
  print(i, '\t', list1[i])
 
print('Negative Index in Ascending Order:')
print('Index \t List elements')
print('----- \t -------------')

for i in range(-len(list1),0):
  print(i, '\t', list1[i])
  
print('Negative Index in Decending Order:')
print('Index \t List elements')
print('----- \t -------------')

for i in range(-1,-len(list1)+1,-1):
  print(i, '\t', list1[i])
