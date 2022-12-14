# 17202. 핸드폰 번호 궁합

A, B, DP1, DP2 = list(input()), list(input()), [], []

for i in range(8):
    DP1 += [int(A[i])]
    DP1 += [int(B[i])]

while len(DP2) != 2:
    DP2 = []
    for i in range(len(DP1)-1):
        DP2 += [(DP1[i] + DP1[i+1]) % 10]
    DP1[:] = DP2[:]

print(str(DP2[0]) + str(DP2[1]))
