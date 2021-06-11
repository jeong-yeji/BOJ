# https://programmers.co.kr/learn/courses/30/lessons/72410


def solution(new_id):
    answer = ""

    # lower case
    new_id = new_id.lower()

    # lower case, number, -, _, . 제외 제거
    for i in new_id:
        if i.isalnum() or i in "-_.":
            answer += i

    # 연속된 마침표 하나로 치환
    while ".." in answer:
        answer = answer.replace("..", ".")

    # 처음과 끝에 있는 . 제거
    if answer and answer[0] == ".":
        answer = answer[1:]
    if answer and answer[-1] == ".":
        answer = answer[:-1]

    # 빈 문자열이면 new_id=a
    if answer == "":
        answer = "a"

    # 16자 이상이면 첫 15자만 남김
    if len(answer) > 15:
        answer = answer[:15]

    # .로 끝나면 제거
    if answer and answer[-1] == ".":
        answer = answer[:-1]

    # 2자 이하면 마지막 문자를 len(new_id)==3까지 붙임
    while len(answer) < 3:
        answer += answer[-1]

    return answer


# 정규표현식 사용..

print("...!@BaT#*..y.abcdefghijklm", "///", solution("...!@BaT#*..y.abcdefghijklm"))
print("z-+.^.", "///", solution("z-+.^."))
print("=.=", "///", solution("=.="))
print("123_.def", "///", solution("123_.def"))
print("abcdefghijklmn.p", "///", solution("abcdefghijklmn.p"))