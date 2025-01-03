def solution(name, yearning, photos):
    answer = []
    yearn = dict(zip(name, yearning))

    for photo in photos:
        score = 0
        yearn_people = set(name) & set(photo)
        for person in yearn_people:
            score += yearn[person]
        answer.append(score)
    return answer
