# 1011 걍 수학문제
# 삼각형 생각 하고 탑찍고 다시 내려온다고 생각

import sys

def calculate(x, y):
    R = y - x
    i = 1
    while(True):
        if(i * i > R):
            i -= 1
            break
        if(i * i == R):
            return 2 * i - 1
        i += 1
    j = R - i * i
    if(j <= i):
        return 2 * i
    else:
        if(j % i == 0):
            return 2 * i - 1 + j // i
        else:
            return 2 * i + j // i

T = int(input())
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    print(calculate(x, y))