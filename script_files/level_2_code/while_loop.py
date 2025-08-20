count = 1
while count <= 5:
    print("count:", count)
    count += 1


# break, continue, pass
for i in range(1, 7):
    if i == 3:
        continue
    if i == 5:
        break
    print(i)