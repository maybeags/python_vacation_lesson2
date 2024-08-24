'''
1. ShoppingCart라는 이름의 클래스를 정의하시오.
    이 클래스는 items라는 리스트를 속성으로 가집니다. 쇼핑 카트에 담긴 상품을 저장합니다.

2. 생성자 메서드:
    __init__(self) 메서드를 정의하여 클래스가 생성될 때, items 리스트를 빈 리스트로 초기화하고
    "장바구니가 생성되었습니다."라는 메시지를 출력하시오.

3. 상품 추가 메서드: add_item(self, item)
    add_item(self, item) 메서드를 정의하시오. 이 메서드는 item을 매개변수로 받아 items 리스트에 추가하고,
    "{item}이 장바구니에 추가되었습니다." 메서드를 출력하시오.

4. 상품 제거 메서드: remove_item(self, item)
    remove_item(self, item) 메서드를 정의하시오. 이 메서드는 item을 매개변수로 받아 items 리스트에서 제거합니다.
    만약 items 리스트에 해당 item이 존재하면 "{item}이 장바구니에서 제거되었습니다."를 출력하시오.
    그렇지 않으면, "{item}이 장바구니에 없습니다." 라는 메시지를 출력하시오.

5. 소멸자 메서드:
    __del__(self) 메서드를 정의하여 객체가 소멸될 때 "장바구니가 비었습니다."를 출력하시오.

실행 예시
cart = ShoppingCart()
cart.add_item("laptop")
cart.add_item("smartphone")
cart.remove_item("laptop")
del cart

실행 결과
장바구니가 생성되었습니다.
laptop이 장바구니에 추가되었습니다.
smartphone이 장바구니에 추가되었습니다.
laptop이 장바구니에서 제거되었습니다.
장바구니가 비었습니다.
'''

class ShoppingCart:

    def __init__(self):
        self.items = []
        print("장바구니가 생성되었습니다.")

    def add_item(self, item):
        self.items.append(item)
        print(f"{item}이 장바구니에 추가되었습니다.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item}이 장바구니에서 제거되었습니다.")
        else:
            print(f"{item}이 장바구니에 없습니다.")

    def __del__(self):
        print("장바구니가 비었습니다.")


cart = ShoppingCart()
cart.add_item("laptop")
cart.add_item("smartphone")
cart.remove_item("laptop")

del cart
