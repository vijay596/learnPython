fruits = ['apple', 'banana', 'cherry']

print(fruits[0])

fruits.append('orange')
print(fruits)    # ['apple', 'banana', 'cherry', 'orange']

fruits.remove('banana')
print(fruits)   # ['apple', 'cherry', 'orange']
print(len(fruits))   # 3

fruits[1] = 'mango'
print(fruits)