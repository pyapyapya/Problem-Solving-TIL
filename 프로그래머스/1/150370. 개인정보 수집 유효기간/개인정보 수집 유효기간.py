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

def is_expired(today, end_date):
    today = list(map(int, today.split(".")))
    end_date = list(map(int, end_date.split(".")))
    return today > end_date

def solution(today, terms, privacies):
    answer = []
    terms = dict([term.split(" ") for term in terms])
    for idx, privacy in enumerate(privacies, 1):
        start_date, term = privacy.split(" ")
        end_date = get_end_date(start_date, int(terms[term]))
        if is_expired(today, end_date):
            answer.append(idx)
    answer = sorted(answer)
    return answer