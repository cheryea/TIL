# 2nd_dimenstion

mat = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
]

# 1. mat[i][j]의 형태를 활용해서
# 1, 2, 3, 4, 5, 6 ... 16 순서대로 출력
for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(mat[i][j], end=' ')

print("")

# 2. 1, 5, 9, 13 / 2, 6, 10, 14
    # 즉, 세로로 출력해보기
for j in range(len(mat[0])):
    for i in range(len(mat)):
        print(mat[i][j], end=' ')

print("")

# 3. 1 + 5 + 9 + 13 / 2 + 6 + 10 + 14
    # 즉, 세로를 더해서 새로운 리스트 만들어보기

total = []

for i in range(len(mat)):
    tmp = 0
    for j in range(len(mat)):
        tmp += mat[j][i]
    total.append(tmp)
print(total)


# 추가 : 1부터 시작하는 n * m 크기의 2차원 배열 만들기


    
