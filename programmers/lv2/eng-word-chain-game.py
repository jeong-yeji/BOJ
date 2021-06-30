# https://programmers.co.kr/learn/courses/30/lessons/12981


def solution(n, words):
    for idx, word in enumerate(words[1:], start=1):
        if words[idx - 1][-1] != word[0] or word in words[: idx - 1]:
            return [idx % n + 1, idx // n + 1]
    return [0, 0]


print(
    solution(
        3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
    )
)
print(
    solution(
        5,
        [
            "hello",
            "observe",
            "effect",
            "take",
            "either",
            "recognize",
            "encourage",
            "ensure",
            "establish",
            "hang",
            "gather",
            "refer",
            "reference",
            "estimate",
            "executive",
        ],
    )
)
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))