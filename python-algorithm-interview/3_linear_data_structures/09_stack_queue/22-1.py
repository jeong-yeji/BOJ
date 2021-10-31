# daily-temperatures


class Solution:
    def dailyTemperatures(self, temperatures):
        stack, res = [], [0] * len(temperatures)
        for idx, t in enumerate(temperatures):
            # 현재 온도 > 스택값 => 정답 처리
            while stack and t > temperatures[stack[-1]]:
                last = stack.pop()
                res[last] = idx - last
            stack.append(idx)
        return res
