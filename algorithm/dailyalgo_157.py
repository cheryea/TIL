def solution(n):
    answer = 0
    while n != 1:
        answer += 1
        if n % 2 == 0:
            n = n // 2
        else: # 1보다 큰 홀수인데, 1은 여기 올 수 없음.
            n = n * 3 + 1
    return answer
