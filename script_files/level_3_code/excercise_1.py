"""
Exercises for You
Create a string "Python Programming" and:
Print first 6 characters.
Convert to uppercase.
Replace "Python" with "Java".

2. Create a list of 5 cities and:
Add one new city.
Remove one city.
Print the final list.

3. Create a tuple of 3 subjects and print the second subject.

4. Create a set of numbers with duplicates, and show that duplicates are removed.
5. Create a dictionary for your profile with keys: name, age, city, skill. Print it.
"""

language = "Python Programming"
print(language[0:6])
lang_upper = language.upper()
repl = language.replace('Python', 'Java')
print(repl)

print(40 * '*')
print("task 2")
print(40 * '*')

cities = ['Nellore', 'Vijayawada', 'Tirupati', 'Visakhapatnam', "Guntur"]

cities.append('kakinada')
cities.remove('Tirupati')
print(cities)

print(40 * '*')
print("task 3")
print(40 * '*')

subjects = ('english', 'telugu', 'kannada')
print(subjects[1])

print(40 * '*')
print("task 4")
print(40 * '*')

numbers = {1,23, 3, 3, 5, 6}
print(numbers)

print(40 * '*')
print("task 5")
print(40 * '*')

details = {'name': 'Vijay', 'age': 28, 'skill': ['python', 'scala']}
print(details['skill'][0])
