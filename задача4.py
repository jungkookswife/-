'''
У вас есть несколько камней известного веса w1, …, wn. Напишите программу, которая распределит камни в две кучи так, что разность весов этих двух куч будет минимальной.
Исходные данные
Ввод содержит количество камней n (1 ≤ n ≤ 20) и веса камней w1, …, wn (1 ≤ wi ≤ 100 000) — целые, разделённые пробельными символами.
Результат
Ваша программа должна вывести одно число — минимальную разность весов двух куч.
'''

n = int(input())
weights = list(map(int, input().split()))

total = sum(weights)
dp = [[False] * (total+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = True

for i in range(1, n+1):
    for j in range(1, total+1):
        if j < weights[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j] or dp[i-1][j-weights[i-1]]

diff = float('inf')
for j in range(total//2, -1, -1):
    if dp[n][j]:
        diff = total - 2 * j
        break

print(diff)