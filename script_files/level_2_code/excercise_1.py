"""
1. Write a program that prints numbers from 1 to 20.

Skip multiples of 3.
Stop if the number reaches 15.
2. Write a while loop that asks for a password until the user enters "python123".

If correct → print "Access Granted".
Otherwise → ask again.

"""
for i in range(1, 20):
    if i % 3 == 0:
        continue
    if i == 15:
        break
    print(i)



while True:
    password = input("Enter password python123: ")
    if password == 'python123':
        print("Access Granted")
        break
    else:
        print("Wrong password, try again.")


