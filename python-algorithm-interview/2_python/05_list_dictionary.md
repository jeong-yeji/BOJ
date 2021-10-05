# 05_list, dictionary

## list

> 리스트(list)란 순서대로 저장하는 시퀀스이자 변경 가능한 목록(Mutable List)으로 입력 순서가 유지됨. 내부적으로는 **요소에 대한 포인터 목록을 갖고 있는 구조체**로 선언된 객체로 구현됨.

### 리스트의 주요 연산 시간 복잡도

| 연산           | 시간 복잡도 | 설명                                                             |
| -------------- | ----------- | ---------------------------------------------------------------- |
| len(a)         | O(1)        |
| a[i]           | O(1)        |
| a[i:j]         | O(k)        | k개의 요소를 가져오기 위해 k개에 대한 조회가 필요                |
| x in a         | O(n)        | 요소가 존재하는지 순차 탐색으로 확인                             |
| a.count(x)     | O(n)        |
| a.index(x)     | O(n)        |
| a.append(x)    | O(1)        | 리스트 마지막에 요소 추가                                        |
| a.insert(i, x) | O(n)        | 특정 위치에 요소 추가                                            |
| a.pop()        | O(1)        | 리스트 마지막 요소 추출                                          |
| a.pop(0)       | O(n)        | 리스트 첫번째 요소 추출. 전체 복사가 필요하므로 O(n) 시간이 소요 |
| del a[i]       | O(n)        | i에 따라 다르며 최악의 경우 O(n)                                 |
| a.remove(x)    | O(n)        |
| a.sort()       | O(n log n)  | Timsort를 사요하여 정렬. 최선의 경우 O(n) 소요                   |
| min(a), max(a) | O(n)        | 선형 탐색                                                        |
| a.reverse()    | O(n)        |

---

## dictionary

### 파이썬 딕셔너리의 특징

-   키/값 구조로 이루어짐
-   입력 순서가 유지됨(python 3.7+)
-   내부적으로 해시 테이블(Hash Table)로 구현됨

### 딕셔너리의 주요 연산 시간 복잡도

| 연산           | 시간 복잡도 | 설명                  |
| -------------- | ----------- | --------------------- |
| len(a)         | O(1)        |
| a[key]         | O(1)        | 키로 조회하여 값 반환 |
| a[key] = value | O(1)        | 키/값 삽입            |
| key in a       | O(1)        | 키의 존재 여부 확인   |

### 딕셔너리 모듈

-   collections.OrderedDict()

    입력 순서가 유지되는 딕셔너리로 python 3.6-에서 사용함.

-   collections.defaultdict()

    존재하지 않는 키를 조회할 경우, 에러 메시지를 출력하지 않고 디폴트 값을 기준으로 해당 키에 대한 딕셔너리 아이템을 생성함.

    ```python
        a = collections.defaultdict(int)
        a['A'] = 5
        a['B'] = 4
        # a : defaultdict(<class 'int'>, {'A': 5, 'B': 4})

        a['c'] += 1 # default value == 0
        # a : defaultdict(<class 'int'>, {'A': 5, 'B': 4, 'C': 1})
    ```

-   collections.Counter()

    요소의 값을 키로 하고 개수를 값 형태로 만들어 카운팅하여 딕셔너리로 리턴

    ```python
        a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
        b = collections.Counter(a)
        # b : Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1})

        # 가장 빈도 수가 높은 요소 추출
        b.most_common(2) # [(5, 3), (6, 2)]
    ```
