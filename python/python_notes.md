# TIL | 파이썬 하다 헷갈린 포인트들

## 리스트 컴프리헨션
```
team = [active_users.pop() for _ in range(team_size)]
```
```
for _ in range(5):
    do_something()
```
- `_` 는 값 안 쓸 때
- 반복 횟수만 필요할 때 사용

## set
- 순서 없음
- 중복 제거
- in 연산 빠름
  ```
  if 2 in s:
    pass
  ```

## i % n
```
for i in range(10):
    print(i % 4, end = " ")
# 값: 0 1 2 3 0 1 2 3 0 1
```
- 0 ~ n-1 반복
- 패턴 반복할 때 자주 씀

## append / extend
```
lst = [1, 2]
lst.append([3, 4])
# 값: [1, 2, [3, 4]]
```
- append: 하나로 들어감
```
  lst = [1, 2]
lst.extend([3, 4])
# [1, 2, 3, 4]
```
- extend, +=: 풀어서 들어감

## find / count / in
```
text = "banana"
```
```
"a" in text     # 있냐
text.count("a") # 몇 개냐
text.find("a")  # 어디냐
```

## / 와 //
```
5 / 2   # 2.5
5 // 2  # 2
```
- / : 실수
- // : 몫 (내림)

## 리스트에서 리스트 빼기
```
numbers = [1, 2, 3, 4, 5]
remove = [2, 4]

result = [x for x in numbers if x not in remove]
print(result) # 값: [1, 3, 5]
```
- 컴프리헨션으로 처리

