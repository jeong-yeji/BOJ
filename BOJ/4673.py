# 셀프 넘버
# 양의 정수 n에 대해 d(n)을 n과 n의 각 자리수를 더하는 함수 ex) d(75) = 75+7+5 = 87
# n, d(n), d(d(n)), d(d(d(n)))과 같이 무한 수열 가능
# n은 d(n)의 생성자
# 생성자가 없는 수가 셀프 넘버
# 10000 이하의 셀프 넘버 출력

# 방법 1
def selfnumber1():
    num_set = set(range(1, 10001))
    remove_set = set()

    for n in num_set:
        a = list(map(int, str(n)))
        remove_set.add(n + sum(a))

    result_set = sorted(num_set - remove_set)

    for res in result_set:
        print(res)


selfnumber1()

# set은 add로 추가, 차집합 연산 가능, set은 순서가 없으므로 정렬 필요

# 방법 2
def selfnumber2():
    remove_set = set()

    for i in range(10001):
        num = list(map(int, str(i)))
        remove_set.add(i + sum(num))

    for i in range(10001):
        if i not in remove_set:
            print(i)


selfnumber2()