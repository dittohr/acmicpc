list = []

for i in range(9):
    numbers = int(input())
    list.append(numbers)

print(max(list))
print(list.index(max(list)) + 1)