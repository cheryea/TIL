from product import Product

# Inventory 클래스: 상품을 관리
class Inventory:

    # 생성자: 빈 상품 목록 초기화
    def __init__(self):
        self.products = {}  # key: 상품명, value: Product 객체

    # 상품 등록 (같은 이름이면 덮어쓰기)
    def set_product(self, name, price, stock):
        self.products[name] = Product(name, price, stock)
        print(f"✅ 상품 등록: {name} / {price}원 / {stock}개")

    # 상품 조회
    def get_product(self, name):
        return self.products.get(name)

    # 현재 상품 목록 출력
    def show_products(self):
        print("\n📦 현재 상품 목록")
        if not self.products:
            print("상품이 없습니다.")
            return
        for name, product in self.products.items():
            print(f"- {name} | 가격: {product.price}원 | 재고: {product.stock}개")
