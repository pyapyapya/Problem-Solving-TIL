def get_oper_priority(arr, check, operator, oper_priority, cnt):
    if cnt == 3:
        oper_priority.append(arr[:])
        return
    
    for i in range(3):
        if not check[i]:
            check[i] = True
            arr.append(operator[i])
            get_oper_priority(arr, check, operator, oper_priority, cnt+1)
            arr.pop()
            check[i] = False

def solution(expression):
    answer = 0
    arr = []
    check = [False for _ in range(3)]
    operator = ['+', '-', '*']
    oper_priority = []
    
    get_oper_priority(arr, check, operator, oper_priority, 0)
    
    expr_nums = []
    expr_opers = []
    
    digit = ''
    for term in expression:
        if term.isdigit():
            digit += term
        else:
            expr_nums.append(int(digit))
            expr_opers.append(term)
            digit = ''
            
    if digit != '':
        expr_nums.append(int(digit))
    
    for oper_priors in oper_priority:
        expr_num = expr_nums[:]
        expr_oper = expr_opers[:]
        for idx, oper_prior in enumerate(oper_priors):
            total = 0
            while oper_prior in expr_oper:
                term = 0
                oper_idx = expr_oper.index(oper_prior)
                term1 = expr_num.pop(oper_idx)
                term2 = expr_num.pop(oper_idx)
                oper = expr_oper.pop(oper_idx)
                if oper == '+':
                    term = term1 + term2
                elif oper == '-':
                    term = term1 - term2
                elif oper == '*':
                    term = term1 * term2 
                expr_num.insert(oper_idx, term)
                if len(expr_num) == 1:
                    answer = max(answer, abs(term))
    
    return answer
