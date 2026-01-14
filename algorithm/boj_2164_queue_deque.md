### 문제
N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.

이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 버린 카드들은 순서대로 1 3 2가 되고, 남는 카드는 4가 된다.

N이 주어졌을 때, 버린 카드들을 순서대로 출력하고, 마지막에 남게 되는 카드를 출력하는 프로그램을 작성하시오.

### 입력
첫째 줄에 정수 N(1 ≤ N ≤ 1,000)이 주어진다.

### 출력
첫째 줄에 버리는 카드들을 순서대로 출력한다. 제일 마지막에는 남게 되는 카드의 번호를 출력한다.

```
# 입력
input_value = int(input())

# 1 ~ 입력값을 리스트로 만들기
lst = [i for i in range(1, input_value+1)]
# 최종 값을 담을 리스트
result = []

# 1장이 남을 때 까지 반복
while len(lst) > 1:
    # 인덱스 0번째(맨위) 카드를 result에 넣는다.
    result.append(lst.pop(0))
    # 인덱스 0번째(맨위) 카드를 다시 lst에 넣는다.
    lst.append(lst.pop(0))

# 마지막 남은 카드를 result에 넣는다.
result.append(lst.pop(0))
print(result)
```

결과 : 틀렸습니다<br>
deque 와 print(*result) 로 해결
### deque
deque는 앞과 뒤에서 데이터를 빠르게 넣고/빼기 위한 자료구조

리스트 ❌ → 배열<br>
deque ⭕ → 양방향 연결 구조

| 동작     | 코드              | 설명     |
| ------ | --------------- | ------ |
| 맨 앞 추가 | `appendleft(x)` | 앞에 넣기  |
| 맨 뒤 추가 | `append(x)`     | 뒤에 넣기  |
| 맨 앞 제거 | `popleft()`     | 앞에서 빼기 |
| 맨 뒤 제거 | `pop()`         | 뒤에서 빼기 |


print(*result) 에서 *란 언패킹을 해줌
<br>
## 최종코드

```
from collections import deque

input_value  = int(input())

lst = deque(range(1, input_value + 1))
result = []

while len(lst) > 1:
    result.append(lst.popleft())
    lst.append(lst.popleft())
result.append(lst.popleft())
print(*result)
```

