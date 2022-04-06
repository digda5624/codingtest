str = input()
cpy = list(str)
rev = list(str)
rev.reverse()
N = len(rev)
cnt = 0
#기준점을 세우고 대칭인지 파악하기
#짝수일 경우에는 처음에 기준점이 어렵다 첫번째만 기준점 생각해주자
# 문자열 뒤집는 경우 다루는 함수를 더 찾아봐야겠다.

if(N % 2 == 0):
    if(cpy[:N // 2 -1] == rev[:N // 2 - 1]):
        cnt = N

for i in range(N // 2, N):
    if(cpy[i:]) == rev[N - i:2 * N - 2 * i]:
        cnt = 2 * i
        break
    if(cpy[i + 1:] == rev[N - i:2 * N - 2 * i - 1]):
        cnt = 2 * i + 1
        break

print(cnt)