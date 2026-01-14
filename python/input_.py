# 7

# number = int(input())

# 4 2 10          # n / w / L
# 7 4 5 6         # list
# input_value = input()

# 과정
input_value = "4 2 10"
input_value = input_value.split() # ['4', '2', '10']
input_value = map(int, input_value)
# map(fun, list) => list의 각각의 원소에 func을 통과시켜 결과를 반환한다.
# [x, y, z] => [f(x), f(y), f(z)]
n, w, L = input_value

# 결과물
n, w, L = map(int, input().split())
lst = list(map(int,input().split()))


# n, w, l, lst를 쓰는 로직

# 입력시간을 줄일때 사용 함.
# 로직의 맨 위에 작성
import sys
input = sys.stdin.readline

# 출력
print(1, 2, 3, 4) # 원소들 사이에 공백이 들어감
print(1, 2, 3, 4, sep="/") # 원소들 사이에 값을 끼워넣을 수 있음
print(*[1, 2, 3, 4]) # 리스트를 분해해서 하나씩 출력함