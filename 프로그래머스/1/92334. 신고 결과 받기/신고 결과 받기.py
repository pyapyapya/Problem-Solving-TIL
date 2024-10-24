def solution(id_list, reports, k):
    answer = []
    ban_list = {_id: 0 for _id in id_list}
    report_dict = {}

    for report in reports:
        report_id, ban_id = report.split(" ")
        if report_id not in report_dict:
            report_dict[report_id] = set()
        # if ban_id report_dict[report_id]
        report_dict[report_id].add(ban_id)

    for ban_ids in report_dict.values():
        for ban_id in ban_ids:
            ban_list[ban_id] += 1
    
    ban_list = [ban_id for ban_id, count in ban_list.items() if count >= k]
    for _id in id_list:
        if _id not in report_dict:
            answer.append(0)
            continue
        count = len(set(report_dict[_id]) & set(ban_list))
        answer.append(count)
    return answer