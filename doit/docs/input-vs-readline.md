# input vs sys.stdin.readline

## input
- prompt message 출력 가능
- 개행문자 삭제 후 리턴 -> rstrip() 함수 적용 후 리턴


## sys.stdin.readline
- prompt message 출력 불가
- 개행문자를 포함해 리턴

---

`input()`은 `sys.stdin.readline`보다 느림!!

```
import sys
input = sys.stdin.readline
input()
```