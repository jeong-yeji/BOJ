# https://programmers.co.kr/learn/courses/30/lessons/12906


def solution(arr):
    answer = []
    prev = ""
    for item in arr:
        if prev != item:
            answer.append(item)
            prev = item
    return answer


# 리스트 슬라이싱 이용하면 빈 리스트에도 가능
# 근데 리스트를 반환해서 item을 리스트로 처리해야됨

print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))
