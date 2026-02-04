from user import User
from inventory import Inventory
from payment import CashPayment, CardPayment

# 1. 사용자 생성
user = User("한별", cash=10000, card_limit=50000)

# 2. 상품 인벤토리 생성
inv = Inventory()

# 3. 상품 등록 (같은 이름이면 덮어쓰기)
inv.set_product("키보드", 2000, 5)
inv.set_product("키보드", 2000, 1)  # 기존 등록 덮어쓰기

# 4. 현재 상품 목록 출력
inv.show_products()

# 5. 결제 수단 생성
cash = CashPayment()  # 현금 결제 객체
card = CardPayment()  # 카드 결제 객체

# 6. 상품 구매
user.buy(inv, "키보드", cash)  # 현금 결제
user.buy(inv, "키보드", card)  # 카드 결제
