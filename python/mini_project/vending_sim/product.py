# Product 클래스: 상품 정보를 저장
class Product:
    # 생성자: 이름, 가격, 재고 초기화
    def __init__(self, name, price, stock):
        self.name = name   # 상품명
        self.price = price # 가격
        self.stock = stock # 재고 수량
