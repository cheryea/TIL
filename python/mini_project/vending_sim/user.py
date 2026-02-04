# User 클래스: 사용자 정보 및 구매 기능 담당
class User:
    # 생성자: 이름, 현금, 카드 한도 초기화
    def __init__(self, name, cash, card_limit):
        self.name = name        # 사용자 이름
        self.cash = cash        # 현금 잔액
        self.card_limit = card_limit  # 카드 한도

    # 상품 구매 메서드
    def buy(self, inventory, product_name, payment):
        # 인벤토리에서 상품 조회
        product = inventory.get_product(product_name)

        # 상품이 존재하지 않으면 종료
        if not product:
            print("\n❌ 상품이 존재하지 않습니다.")
            return

        # 재고가 없으면 종료
        if product.stock <= 0:
            print("\n❌ 재고가 없습니다.")
            return

        # 구매 시도 출력
        print(f"\n🛒 '{self.name}'님이 '{product.name}' 구매 시도")

        # 결제 시도
        if payment.pay(self, product.price):
            # 결제 성공 → 재고 1 감소
            product.stock -= 1
            print("🎉 구매 성공")
        else:
            # 결제 실패
            print("💥 구매 실패")
