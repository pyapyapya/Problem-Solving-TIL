"""
1. dict에서 key가 없는 경우 할당을 미리 선언해줄 수 있음
    - if report_id not in report_dict:
        report_dict[report_id] = set()
     ---
     => user_reports = {user: set() for user in reports}
    
    - from collections import defaultdict
     
2. 변수명
    - ban_list => report_counts
3. dict get 활용
4. 중복처리
    - reports = list(set(reports))
"""
from collections import defaultdict

def solution(id_list, reports, k):
    answer = []
    reports = list(set(reports))
    report_counts = defaultdict(int)
    user_reports = defaultdict(set)

    for report in reports:
        report_id, ban_id = report.split(" ")
        user_reports[report_id].add(ban_id)
        report_counts[ban_id] += 1

    banned_id = set([ban_id for ban_id, count in report_counts.items() if count >= k])
    for user_id in id_list:
        count = len(user_reports.get(user_id, set()) & banned_id)
        answer.append(count)
    return answer
