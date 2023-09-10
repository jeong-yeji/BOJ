for t in range(int(input())):
    speed, move = 0, 0
    for _ in range(int(input())):
        command = input()
        if command.startswith('1'):
            speed += int(command[2:])
        elif command.startswith('2'):
            speed -= int(command[2:])
            if speed < 0:
                speed = 0
        move += speed
    print(f'#{t + 1} {move}')
