def solution(numbers):
    n = len(numbers)


    for i in range(n):
        number = numbers[i]

        if number != i+1:
            return i+1
        
    return n+1

