def solution(change):
    coins = [500, 400, 100, 50, 10, 5, 1]
    count = 0
    for coin in coins:
        count += change // coin # 몫
        change = change % coin
    
    return count
