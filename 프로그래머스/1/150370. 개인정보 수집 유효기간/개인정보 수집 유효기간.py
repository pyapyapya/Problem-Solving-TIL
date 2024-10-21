def get_end_date(start_date, interval):
    year, month, day = list(map(int, start_date.split(".")))
    day -= 1
    if day == 0:
        month -= 1
        day = 28

    year += (month + interval) // 12
    month = (month + interval) % 12
    if month == 0:
        year -= 1
        month = 12
    return f"{str(year)}.{str(month).zfill(2)}.{str(day).zfill(2)}"

def is_delete(today, end_date):
    today = list(map(int, today.split(".")))
    end_date = list(map(int, end_date.split(".")))
    if today[0] > end_date[0]:
        return True
    elif today[0] == end_date[0] and today[1] > end_date[1]:
        return True
    elif today[0] == end_date[0] and today[1] == end_date[1] and today[2] > end_date[2]:
        return True
    else:
        return False

def solution(today, terms, privacies):
    answer = []
    terms = dict([term.split(" ") for term in terms])
    data = []
    for idx, privacy in enumerate(privacies, 1):
        start_date, term = privacy.split(" ")
        end_date = get_end_date(start_date, int(terms[term]))
        privacy = {
            "id": idx,
            "start_date": start_date,
            "end_date": end_date,
            "term": term,
        }
        data.append(privacy)
    
    for d in data:
        if is_delete(today, d["end_date"]):
            answer.append(d["id"])
    answer = sorted(answer)
    return answer