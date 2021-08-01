# 게임 개발


def solution(n, m, x, y, d, input_list):
    direction = d
    map_array = []
    for i in input_list:
        map_array.append(list(map(int, i)))

    visited = [[0] * m] * n
    visited[x][y] = 1  # 현재 좌표 방문 처리

    # 북동남서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def turn_left():
        global direction
        direction -= 1
        if direction == -1:
            direction = 3

    cnt = 1
    turn_time = 0

    while True:
        turn_left()

        nx = x + dx[direction]
        ny = y + dy[direction]

        # 회전 후 정면에 가보지 않은 칸이 존재하면 이동
        if visited[nx][ny] == 0 and map_array[nx][ny] == 0:
            visited[nx][ny] = 0
            x, y = nx, ny
            cnt += 1
            turn_time = 0
            continue
        else:  # 회전 후 정면에 가본 칸이 없거나 바다인 경우
            turn_time += 1

        # 네방향 모두 갈 수 없을 때
        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]

            # 뒤로 갈 수 있으면 이동
            if map_array[nx][ny] == 0:
                x, y = nx, ny
            else:  # 뒤가 바다로 막힌 경우
                break

            turn_time = 0

    return cnt


print(solution(4, 4, 1, 1, 0, [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]))
