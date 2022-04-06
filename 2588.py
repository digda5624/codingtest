n = int(input())
m = input()
numlist = list(map(int, m))
numlist.reverse()

for i in numlist:
    print(i * n)
print(n * int(m))


