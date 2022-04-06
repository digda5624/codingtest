
L, C = map(int, input().split())
alpha = list(input().split())
alpha.sort()

aeiou = ['a', 'e', 'i', 'o', 'u']
# 기억해두기 차집합
mo = [x for x in alpha if x in aeiou]
ja = [x for x in alpha if x not in aeiou]

if(len(mo) >= 1 and len(ja) >= 2):
    for i in range(len(mo)):
        for j in range(len(ja)):
            for k in range(j+1, len(ja)):
                strs = [mo[i], ja[j], ja[k]]
                rest = mo[i:] + ja[j:]
                print(rest)