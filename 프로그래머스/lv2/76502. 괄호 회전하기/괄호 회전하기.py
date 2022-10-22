"""

"""
def solution(s):
    answer = 0
    if len(s) % 2 == 1:
        return 0
    
    for i in range(len(s)):
        string = s[i:] + s[:i]
        
        bracket = []
        
        check = False
        for char in string:
            if char == '(' or char == '{' or char == '[':
                bracket.append(char)
            else:
                if len(bracket) <= 0:
                    check = True
                    break
                    
                if char == ')' and bracket[-1] == '(':
                    bracket.pop()
                elif char == '}' and bracket[-1] == '{':
                    bracket.pop()
                elif char == ']' and bracket[-1] == '[':
                    bracket.pop()
                else:
                    check = True
                    break
        if not check:
            if len(bracket) == 0:
                answer += 1
    return answer

"""
1. [)(] 
2. ][)(
3. (][)
4. )(][
"""