import random

# 전체 참가자 명단
names = [
    '김도윤', '박하린', '최민재', '이서연', '정우진',
    '한예린', '윤태현', '오지후', '배수아', '강민호',
    '송지안', '이상호', '임서준', '문채원', '신유찬',
    '조아린', '백현우', '노지민', '차은결', '홍세린'
]

# 제외될 참가자 리스트 초기화
removed_users = []

# 사용자로부터 제외할 인원 입력받기
while True:
    input_data = input("'랜덤 조 짜기'에서 제외할 인원의 이름을 입력해 주세요. (나가기:q) ")
    print(f"'{input_data}'를 입력받았습니다.")

    # 'q' 입력 시 입력 종료
    if input_data == 'q':
        print(f"{removed_users}를 제외하고 조를 편성합니다.")
        break
    
    # 이미 입력한 이름인 경우
    if input_data in removed_users:
        print("이미 입력한 이름입니다.")
    
    # 참가자 명단에 존재하면 제외 리스트에 추가
    elif input_data in names:
        removed_users.append(input_data)
        print(removed_users)
    
    # 참가자 명단에 없는 이름 입력 시
    else:
        print("다시 입력해 주세요")

# 제외된 사람을 제외한 참가자 리스트 생성
active_users = list(set(names) - set(removed_users))
print("참가자 명단:", active_users)

# -------------------------------
# 팀 구성 함수
# -------------------------------
def make_team(active_users, team_size=3):
    """
    참가자 리스트를 받아서 랜덤으로 팀을 구성하는 함수
    - active_users: 팀에 포함될 참가자 리스트
    - team_size: 한 팀당 인원 수 (기본 3명)
    """
    random.shuffle(active_users)  # 참가자 리스트 무작위 섞기
    teams = []

    # 팀을 기본 인원 수만큼 만들어 추가
    while len(active_users) >= team_size:
        team = [active_users.pop() for _ in range(team_size)]
        teams.append(team)

    # 남은 인원 1~2명을 기존 팀에 순차적으로 배치
    for i, user in enumerate(active_users):
        teams[i].append(user)

    return teams

# 팀 생성
teams = make_team(active_users)

# -------------------------------
# 팀 출력
# -------------------------------
for team_id, team in enumerate(teams, start=1):  # 팀 번호를 1번부터 시작
    print(f"{team_id}조 : {team} (총 {len(team)}명)")
