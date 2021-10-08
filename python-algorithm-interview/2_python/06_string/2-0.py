class Solution:
    def reverseString(self, s) -> None:
        # Do not return anything, modify s in-place instead.
        s.reverse()

# 리트코드에서는 공간복잡도를 O(1)로 제한했기 때문에 s = s[::-1] 사용 시 오류 발생
# => s[:] = s[::-1] 을 이용하면 사용 가능
