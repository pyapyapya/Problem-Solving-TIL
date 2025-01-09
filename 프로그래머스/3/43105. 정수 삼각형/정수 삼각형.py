def solution(t):
    answer = 0
    dp = [t[0]]
    for j in range(1, len(t)):
        d = []
        for i in range(len(t[j])):
            if i == 0:
                d.append(dp[j-1][0] + t[j][0])
            elif 0 < i < len(t[j])-1:
                d.append(max(dp[j-1][i-1] + t[j][i], dp[j-1][i] + t[j][i]))
            else:
                d.append(dp[j-1][-1] + t[j][-1])

        dp.append(d)
    answer = max(dp[-1])
    return answer