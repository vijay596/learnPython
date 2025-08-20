def greet(name):
    return f"Hello! {name}"

result = greet("vijay")
print(result)
print(greet("sujay"))


def simple_intrest(principal, rate, time):
    return (principal * rate * time)/100

print(simple_intrest(100000, 2, 12))


#positional arguments

def add(a, b):
    print('sum:', a + b)
add(10, 20)

#keyword arguments
def introduce(name, age):
    print(f"my name is {name}, i am {age} years old.")

introduce(age=28, name='vijay')


#default arguments
def greet1(name='Guest'):
    print(f"Hello!, {name}")
greet1()

def total_sum(*numbers):
    print("Numbers:", numbers[0])
    print("Sum:", sum(numbers))

total_sum(10, 20, 30, 40)


def person_info(**details):
    print("Details:", details)


person_info(name="Vijay", age=25, city="Nellore")





