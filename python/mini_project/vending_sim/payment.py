from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, user, product):
        pass


class CashPayment(Payment):
    def pay(self, user, price):
        if user.cash < price:
            print("❌ 현금 부족")
            return False

        user.cash -= price
        print(f"💵 현금 {price}원 결제 (남은 금액: {user.cash}원)")
        return True

class CardPayment(Payment):
    def pay(self, user, price):
        if user.card_limit < price:
            print("❌ 카드 한도 초과")
            return False

        user.card_limit -= price
        print(f"💳 카드 {price}원 결제 (남은 금액: {user.card_limit}원)")
        return True
