from collections import deque

print(deque(range(5)))
# deque([1, 2, 3, 4])

q = deque(range(5))

# 데이터 삽입
q.append('a')
print(q)

q.appendleft('b')
print(q)

# 데이터의 삭제
popped_el = q.pop()
print(q)
print(popped_el)

popped_el = q.popleft()
print(q)
print(popped_el)
