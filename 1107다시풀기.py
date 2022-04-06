# 리모컨 문제 숫자 조합으로 가는 것 같다.
# 제일 앞자리 부터 진행하는데 자리수랑 같게 안되면 바로 flag세우고 최대숫자 박거나 최소숫자 박아야함

def a(N, i):
    for j in N:
        if(i < j):
            k = N.index(j)
            if(k == 0):
                return (N[k], N[k])
            return (N[k-1], N[k])
    return (N[len(N) - 1], N[len(N) - 1])

def func():
    return
N = int(input())
Nlist = list(map(int, list(str(N))))
M = int(input())
number = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
ex = set(map(int, input().split()))
number = list(number - ex)
number.sort()
flag = True
one = ""
two = ""
count1 = 0
count2 = 0
count3 = 0

if(len(number) > 0):
    for i in Nlist:
        if(flag is True and i in number):
            one = one + str(i)
            two = two + str(i)
            count1 += 1
            count2 += 1
        elif(flag is True and i not in number):
            flag = False
            x, y = a(number, i)
            one = one + str(x) #작은거
            two = two + str(y) #큰거
            count1 += 1
            count2 += 1
        else:
            one = one + str(number[len(number) - 1])
            two = two + str(number[0])
            count1 += 1
            count2 += 1
    count1 += abs(N - int(one))
    count2 += abs(N - int(two))
    count3 += abs(N - 100)
    f = [count1, count2, count3]
    f.sort()
    print(f[0])

else:
    count3 += abs(N - 100)
    print(count3)