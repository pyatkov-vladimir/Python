from typing import List, FrozenSet
string = 'Oasis' #1
int = 1994 #2
float = 29.08 #3
bytes = b'bytes' #4

spisok: list[str] = ["Rock n Roll Star", "Shakermaker"] #5

tuple = tuple('Bring It on Down') #6

set = set('аргентина манит негра') #7
frozen_set: frozenset[str] = frozenset('курочка ряба') #8
dict = {'band': 'Oasis',
         'rating': 10,
         10: True}   #9

print(type(string), string)
print(type(int), int)
print(type(float), float)
print(type(bytes), bytes)
print(type(spisok), spisok)
print(type(tuple), tuple)
print(type(set), set)
print(type(frozen_set), frozen_set)
print(type(dict), dict) #10

a1 = 'Cat'
a2 = 'Dog'
a3 = a1 + a2
print(a3)   #11

b2 = 150
b1 = 11
b3 = b1 + b2
print(b3) #12

b4 = b2/b1
print(b4)#13

b5 = b2*b1
print(b5) #14

b6 = b2//b1
print(b6) #15

b7 = b2 % b1
print(b7)

print((7+12)**3+7*4-44/2**4)


