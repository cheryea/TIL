
def solution(n):
    # 1. 1 ~ n까지 숫자를 확인한다.
    # 2. 숫자에 3, 6, 9가 포함되어있는지 확인한다.
        # count를 1 늘려준다.
    
    answer = 0

    # 1
    for num in range(1, n+1):
        str_n = str(num)
        # if 3일 들어있니 / 6이 들어있니 / 9가 들어있니
        if '3' in str_n or '6' in str_n or '9' in str_n:
            answer += 1

    return answer
