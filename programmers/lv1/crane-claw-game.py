# https://programmers.co.kr/learn/courses/30/lessons/64061


def solution(board, moves):
    answer = 0
    delStack = []

    for move in moves:
        move -= 1
        delItem = 0

        for i in range(len(board)):
            if board[i][move] != 0:
                delItem = board[i][move]
                board[i][move] = 0
                break

        if delItem != 0 and len(delStack) != 0 and delStack[-1] == delItem:
            answer += 2
            delStack.pop()
        else:
            delStack.append(delItem)

    return answer


# 다른 풀이
# delItem 찾았을 때 append 하고
# length>1이면 끝에 두개 비교해서 같으면 2개 빼기..


board = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1],
]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, moves))