arr = [10,3,45,6,8,23,42,56,30]
max = min = arr[0]
for num in arr:
    if num > max:
        smax = max
        max = num
    elif (num > max and num != max):
        smax = num
    if num < min:
        smin = min
        min = num
    elif (num < min and num != num):
        smin = num
    print()

print("Largest:",max)
print("Second Largest:",smax)
print("Smallest:",min)
print("Second Smallest:",smin)
