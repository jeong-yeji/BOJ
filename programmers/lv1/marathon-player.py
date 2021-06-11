# https://programmers.co.kr/learn/courses/30/lessons/42576


def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]


# Counter 이용
# import collections
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(
    solution(
        ["marina", "josipa", "nikola", "vinko", "filipa"],
        ["josipa", "filipa", "marina", "nikola"],
    )
)
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))