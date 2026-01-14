
### 상품 리스트를 카테고리별로 분류하여 딕셔너리를 만드세요.
```
products = [
    {"category": "전자제품", "name": "키보드"},
    {"category": "의류", "name": "티셔츠"},
    {"category": "전자제품", "name": "마우스"},
    {"category": "전자제품", "name": "노트북"},
    {"category": "식품", "name": "사과"},
    {"category": "식품", "name": "배"},
    {"category": "의류", "name": "청바지"}
]

grouped_data = {}

# grouped_data는 처음에 빈 딕셔너리 {}
# → 아직 어떤 category도 key로 존재하지 않는 상태

for item in products:
    category = item["category"]
    name = item["name"]

    # 현재 category가 grouped_data에 없다면
    # → 처음 등장한 카테고리이므로 빈 리스트를 먼저 생성
    if grouped_data.get(category) is None:
        grouped_data[category] = []

    # 해당 카테고리 리스트에 name 추가
    grouped_data[category].append(name)
    
    
print(f"그룹화 결과: {grouped_data}")
```
