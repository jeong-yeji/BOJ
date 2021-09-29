# 평균은 넘겠지
# 정수를 입력받아 그 수만큼 테스트 케이스를 입력 받는다.
# 각 테스트 케이스의 첫 수는 학생 수, 나머지는 n명의 점수(0 이상 100 이하)이다.
# 각 테스트 케이스마다 평균 이상 학생의 비율을 반올림하여 소수점 셋째 자리까지 출력
for _ in range(int(input())):
    case = list(map(int, input().split()))
    avg = sum(case[1:]) / case[0]
    count = 0
    for c in case[1:]:
        if c > avg:
            count += 1
    result = round(count / case[0] * 100, 3)
    print("{:.3f}%".format(result))