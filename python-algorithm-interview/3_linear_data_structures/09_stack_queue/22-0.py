# daily-temperatures

# 시간 초과..
class Solution:
    def dailyTemperatures(self, temperatures):
        res = []
        for idx, temperature in enumerate(temperatures):
            cnt = 0
            for t in temperatures[idx + 1 :]:
                cnt += 1
                if t > temperature:
                    break
            else:
                cnt = 0
            res.append(cnt)
        return res
