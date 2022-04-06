# ** 은 제곱수를 의미한다.
def a(N, r, c):
    global count
    if(N == 0):
        return
    if(0 <= r < 2 ** (N - 1) and 0 <= c < 2 ** (N - 1)):
        count += 0
        r, c = (r, c)
    if (0 <= r < 2 ** (N - 1) and 2 ** (N - 1) <= c < 2 ** N):
        count += 2 ** (2 * N - 2)
        r, c = (r, c - 2 ** (N - 1))
    if (2 ** (N - 1) <= r < 2 ** N and 0 <= c < 2 ** (N - 1)):
        count += 2 ** (2 * N - 1)
        r, c = (r - 2 ** (N - 1), c)
    if (2 ** (N - 1) <= r < 2 ** N and 2 ** (N - 1) <= c < 2 ** N):
        count += 2 ** (2 * N - 2) * 3
        r, c = (r - 2 ** (N - 1), c - 2 ** (N - 1))

    N -= 1
    a(N, r, c)


# def b(N, r, c):
#     global count
#     temp1 = r // 2
#     temp2 = c // 2
#     count += temp1 * (2 ** N) + 4 * temp2
#     return (r % 2, c % 2)
#
# def d(r, c):
#     global count
#     if (r == 0 and c == 0):
#         count += 0
#     elif (r == 0 and c == 1):
#         count += 1
#     elif (r == 1 and c == 0):
#         count += 2
#     else:
#         count += 3

N, r, c = map(int, input().split())
count = 0
a(N, r, c)
print(count)

