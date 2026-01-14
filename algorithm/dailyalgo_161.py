def solution(n):
    # 뒤집는다
    str_n = str(n)
    reversed_n = str_n[::-1]
    
    # 비교한다
    return str_n == reversed_n
