def dfs(word, ans, cnt, depth, arr):
    if depth == 5:
        return ans, cnt

    for a in arr:
        if len(ans) <= depth:
            ans.append(a)
        else:
            ans[depth] = a
        cnt += 1
        if word == "".join(ans):
            return ans, cnt
        else:
            (ans, cnt) = dfs(word, ans, cnt, depth+1, arr)
            if word == "".join(ans):
                return ans, cnt
            else:
                ans.pop()
    return (ans, cnt)

def solution(word):
    answer = 0
    ans = []
    arr = ["A", "E", "I", "O", "U"]
    ans, cnt = dfs(word, ans, 0, 0, arr)
    return cnt