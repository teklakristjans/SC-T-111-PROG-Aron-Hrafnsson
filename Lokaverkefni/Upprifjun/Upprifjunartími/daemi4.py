size = int(input("Input size: "))

arr = []
for i in range(size):
    arr.append(int(input("Enter value {}:".format(i + 1))))

print(max(arr))

highest = arr[0]

for x in range(1, len(arr)):
    if arr[x] > highest:
        highest = arr[x]

print("{} is the highest".format(highest))

