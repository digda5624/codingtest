x = [1, 2, 3, 4, 5, 6]
print(x[3:])
print(x[3:][::-1])
print(x[3:][::1])

s=input()

for i in range(len(s)):
    print(s[i:][::-1])
    print(s[i:])
    print()
    if s[i:]==s[i:][::-1]:
        print(len(s)+i)
        break