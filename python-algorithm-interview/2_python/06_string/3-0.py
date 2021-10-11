# reorder-data-in-log-files


class Solution:
    def reorderLogFiles(self, logs):
        letters, digits = [], []

        for log in logs:
            if log.split()[1].isdigit():  # digit logs
                digits.append(log)
            else:  # letter logs
                letters.append(log)

        # 문자 동일 시, 식별자 순으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits


logs1 = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(Solution().reorderLogFiles(logs1))
logs2 = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
print(Solution().reorderLogFiles(logs2))
