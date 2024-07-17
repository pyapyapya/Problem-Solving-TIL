import sys

input = sys.stdin.readline
n = int(input())
k = int(input())
votes = list(map(int, input().split(" ")))

vote_counts = {}
updated = {}
stack = []
time = 0
for voted_student in votes:
    time += 1
    if voted_student in vote_counts:
        vote_counts[voted_student] += 1
    else:
        if len(stack) < n:
            stack.append(voted_student)
            vote_counts[voted_student] = 1
            updated[voted_student] = time
        else:
            min_votes = min(vote_counts.values())
            candidates = []
            for s in stack:
                if vote_counts[s] == min_votes:
                    candidates.append(s)
            min_time = 1001
            student = 101
            for candidate in candidates:
                if updated[candidate] < min_time:
                    min_time = updated[candidate]
                    student = candidate

            stack.remove(student)
            del updated[student]
            del vote_counts[student]

            stack.append(voted_student)
            vote_counts[voted_student] = 1
            updated[voted_student] = time
        
print(' '.join(map(str, sorted(stack))))
