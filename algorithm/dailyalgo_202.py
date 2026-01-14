def solution(numbers, window):
    answer = []

    for i in range(len(numbers) - window + 1):
        total = sum(numbers[i : i+window])
        answer.append(total)
    
    return answer
solution([4,1,5,0,-4,1,-10], 3)