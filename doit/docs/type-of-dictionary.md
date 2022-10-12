# type of dictionary

## Dictionary

- Python의 기본 dictionary
- 데이터가 무작위 순서로 저장됨
- 존재하지 않는 key를 참조할 때 KeyError 발생

## collections.OrderedDict()

- index를 가짐 -> 데이터가 순서를 가짐

## collections.defaultdict()

- 디폴트값을 가지는 딕셔너리 -> KeyError가 발생하지 않음
- `int_dict = defaultdict(int)` : The dictionary's default value is int

