n=int(input("Enter no of rows:"))
mid = (n+1)/2
i=1
for i in range (n):
    for j in range(n):
        if (j==mid or i==mid):
            print('*', end=" ")
        else:
            print(" ", end=" ")
    print()
