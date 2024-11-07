def solution(citations):
    answer = []
    citations = sorted(citations, reverse=True)
    n = len(citations)
    
    for i, citation in enumerate(citations, start=1):
        h = min(i, citation)
        answer.append(h)
    return max(answer)
