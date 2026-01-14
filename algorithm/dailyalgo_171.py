from collections import Counter, defaultdict
def solution(numbers):
    # 각 숫자들을 돌면서 개수를 셀꺼야.
    # 어디다가 셀거냐? -> list dict
        # list : 뭐가 뭐에 대한 숫자인지 매칭이 안됨
        # dict : 만들겠어.

    count_dic = {}
    # count_dic = defaultdict(int)
    for num in numbers:
        # count_dic.get(key, 기본값)
        count_dic[num] = count_dic.get(num, 0) + 1

        # if count_dic.get(num) == None:
        #     count_dic[num] = 0
        # count_dic[num] += 1

    print(count_dic)
    # print(Counter(numbers)) # 참고 정도만 하세요.

    # 최빈값에 대한 개수 구하기
    # max(count_dic.values())
    max_value = 0
    for key, value in count_dic.items():
        if value >= max_value:
            max_value = value

    # 최빈값을 알아야 함
    # common_values = [key for key, value in count_dic.items() if value == max_value]
    common_values = []
    for key, value in count_dic.items():
        if value == max_value:
            common_values.append(key)
    
    
    # common_value에서 최소값을 구해야 함.
    # min_value = min(common_values)
    min_value = 1000 # 문제의 제한사항의 최대값을 작성
    for value in common_values:
        if value < min_value:
            answer = value
            min_value = value

    return answer


print(solution([1, 1, 2, 2, 2, 3, 3,2, 3, 4, 1, 2, -1, -3, -5 ]))
