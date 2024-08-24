from prettytable import PrettyTable
'''
p 278

1. 클래스 변수

    인스턴스 변수 : 인스턴스마다 서로 다른 값을 가지는 경우
    클래스 변수 : 모든 인스턴스가 동일한 값을 가지는 경우
+-----------+-----------------------------+-------------------------------+
|    구분   |        인스턴스 변수        |          클래스 변수          |
+-----------+-----------------------------+-------------------------------+
|    목적   | 인스턴스마다 다른 값을 저장 | 인스턴스가 공유하는 값을 저장 |
| 접근 방식 |       인스턴스 접근(o)      |        인스턴스 접근(o)       |
|           |        클래스접근(x)        |         클래스 접근(o)        |
+-----------+-----------------------------+-------------------------------+
'''
# table = PrettyTable()
# table.field_names = ["구분", "인스턴스 변수", "클래스 변수"]
# table.add_row(["목적", "인스턴스마다 다른 값을 저장", "인스턴스가 공유하는 값을 저장"])
# table.add_row(["접근 방식","인스턴스 접근(o)", "인스턴스 접근(o)"])
# table.add_row(["","클래스접근(x)", "클래스 접근(o)"])
# print(table)

# class Korean:
#
#     country = "한국"      # 클래스 변수 country
#
#     def __init__(self, name, age, address):
#         self.name = name                    # 인스턴스 변수
#         self.age = age                      # 인스턴스 변수
#         self.address = address              # 인스턴스 변수
#
#
# man = Korean("안근수", 37, "부산광역시 연제구")
# print(man.country)          # 인스턴스 man을 통한 클래스 변수 접근
# print(Korean.country)       # 클래스 Korean을 통한 클래스 변수 접근
# man2 = Korean(name="안근순", age=38, address="서울특별시 종로구")
# print(man2.country)

# 클래스 변수는 클래스를 통해서 접근하는 것이 권장 사양 -> man.country보다는 Korean.country로 작성하라는 의미.

# man2.country = "대한민국"                     # 하지마세요의 사례
# print(man.country)
# print(man2.country)
# man3 = Korean("안근", 40, "광주광역시 북구")
# print(man3.country)

'''
p 279

2. 클래스 메서드

클래스 메서드(class method) : 클래스 변수를 사용하는 메서드

특징 :

1. 인스턴스 또는 클래스로 호출
2. 생성된 인스턴스가 없어도 호출 가능
3. @classmethod 데코레이터(decorator)를 표시하고 작성
4. 매개변수 self를 사용하지 않고 cls를 사용

호출 방식 :

클래스.메서드() -> self를 사용하지 않기 때문에 인스턴스 변수에 접근 불가능. cls를 통해 class 변수에만 접근 가능.

'''

# class Korean2:
#
#     country = "대한민국"    # 클래스 변수
#
#     @classmethod
#     def trip(cls, country):
#         if cls.country == country:
#             print("국내 여행입니다.")
#         else:
#             print("해외 여행입니다.")
#
#
# Korean2.trip("대한민국")            # 객체 생성을 하지 않고 클래스 자체에서 메서드를 호출함.
# Korean2.trip("미국")

'''
Korean2 클래스에 정의된 trip() 메서드는 클래스 메서드임을 알리는 @classmethod로 시작.
첫번째 매개변수인 cls는 class의 축약형. 여기서는 클래스 Korean2를 의미함.
따라서 내부의 cls.country는 Korean2.country와 동일한 의미입니다. 이를 클래스 내부에서는 cls.country로 표기됩니다.
클래스 메서드는 인스턴스를 생성하지 않아도 클래스만으로 호출이 가능, 즉 Korean2.trip(인수)로 호출 가능합니다.

p 280

정적 메서드(static method)

정적 메서드 또한 self를 사용하지 않습니다 -> 이 의미는 인스턴스 변수에 접근하여 사용하는 것이 불가능하다는 의미.
인스턴스를 생성하지 않아도 사용할 수 있다는 점 때문에 클래스 메서드와 비슷합니다.

특징

1. 인스턴스 또는 클래스로 호출 가능
2. 생성된 인스턴스가 없어도 호출 가능
3. @staticmethod 데코레이터를 표시하고 작성
4. 반드시 작성해야 할 매개변수가 없습니다.

정적 메서드는 self, cls를 다 사용하지 않기 때문에 인스턴스 변수와 클래스 변수를 모두 사용하지 않는 메서드를 정의하는 경우에 적절합니다.
정적 메서드는 클래스에 소속돼 있지만, 인스턴스에는 영향을 주지도 않고, 또 영향을 받지도 않습니다.
'''

# class Korean3:
#
#     country = "한국"      # 클래스 변수
#
#     @staticmethod
#     def slogan():       # 클래스 및 인스턴스 변수를 모두 사용하지 않는 정적 메서드
#         print("Imagine you Korea")
#
#
# Korean3.slogan()        # 클래스로 정적 메서드 호출

'''
기본 예제

다음은 가방을 만들 때마다 현재 만들어진 가방이 몇 개인지 계산할 수 있는 Bag 클래스입니다.
'''

# class Bag:
#
#     count = 0           # 클래스 변수
#
#     def __init__(self):         # 생성자
#         Bag.count += 1
#         print("가방이 생산되었습니다.")
#
#     @classmethod
#     def sell(cls):
#         cls.count -= 1
#
#     @classmethod
#     def remain_bag(cls):
#         return cls.count
#
#
# print(f"현재 가방 : {Bag.remain_bag()}")
# bag1 = Bag()
# bag2 = Bag()
# bag3 = Bag()
# print(f"현재 가방 : {Bag.remain_bag()}")
# bag1.sell()
# bag2.sell()
# print(f"현재 가방 : {Bag.remain_bag()}")

'''
응용 예제

1. 다음 지시사항을 일고 이름과 전체 인구수를 저장할 수 있는 Person 클래스를 생성하세요.

지시사항
1. 다음과 같은 방법으로 man과 woman 인스턴스를 생성하세요.
man = Person("james")
woman = Person("emily")

2. man과 woman 인스턴스가 생성되면 다음과 같은 메시지를 출력할 수 있도록 처리하세요.
james is born.
emily is born.

3. 다음 코드를 통해서 전체 인구수를 조회할 수 있도록 처리하세요.
print(f"전체 인구수 : {Person.get_population()}")

4. 다음과 같은 방법으로 man 인스턴스를 삭제하세요.
del man

5. man 인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 처리하세요.
james is dead.

'''
# class Person:
#
#     population = 0
#
#     # 1번 지시사항
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name} is born.")      # 2번 지시사항
#         Person.population += 1
#
#     @classmethod                            # 3번 지시사항
#     def get_population(cls):
#         return Person.population
#
#     def __del__(self):                      # 4번 지시사항
#         print(f"{self.name} is dead.")
#         Person.population -= 1
#
# man = Person("james")
# woman = Person("emily")
# print(f"전체 인구수 : {Person.get_population()}")
# del man
# print(f"전체 인구수 : {Person.get_population()}")


'''
2. 다음 지시사항을 읽고 가게의 매출을 구할 수 있는 Shop 클래스를 구현하세요.

지시사항
1. Shop 클래스는 다음과 같은 클래스 변수를 가지고 있습니다.
    total -> 가게 전체 매출액
    menu_list -> {메뉴명:가격}으로 이루어진 딕셔너리
    menu_list = [ {메뉴명1:가격1}, {메뉴명2:가격2} ]
    
    menu_list =  [{"떡볶이": 3000}, {"순대":3000}, {"튀김":500}, {"김밥":2000}]
    
2. 매출이 생기면 다음과 같은 방식으로 메뉴와 판매량을 작성합니다.
Shop.sales("떡볶이", 1)    # 떡볶이을(를) 1개 판매
Shop.sales("김밥", 2)    # 김밥을(를) 2개 판매
Shop.sales("튀김", 5)    # 튀김을(를) 5개 판매

3. 모든 매출을 작성한 뒤 다음과 같은 방식으로 전체 매출액을 확인합니다.
print(f"매출 : {Shop.total}원")
'''
#
# class Shop:
#     total = 0   # 전체 매출액을 나타는 클래스 변수
#     menu_list = [{"떡볶이": 3000}, {"순대":3000}, {"튀김":500}, {"김밥":2000}]  # 메뉴와 가격정보
#
#     @classmethod
#     def sales(cls, item, quantity):
#         for menu in cls.menu_list:                      # menu_list 내에 있는 0번지부터 3번지까지의 각각의 딕셔너리 menu를 불러옴.
#             if item in menu:                            # 딕셔너리 menu 내에 있는 key값의 일치 여부 확인
#                price = menu[item]                       # key값으로 조회한 value값을 price에 대입
#                print(f"{item}을(를) {quantity}개 판매")
#                total_price = price * quantity           # 클래스 price에 value * quantity한 값을 대입하기 위해 지역 변수 total_price 선언 및 초기화
#                cls.total += total_price                 # total_price를 cls.total에 대입
#
#
#     # @classmethod
#     # def show_total_sales(cls):
#     #     print(f"매출 : {cls.total}원")
#
#
# Shop.sales("떡볶이", 1)    # 떡볶이을(를) 1개 판매
# Shop.sales("김밥", 2)    # 김밥을(를) 2개 판매
# Shop.sales("튀김", 5)    # 튀김을(를) 5개 판매
#
# print(f"매출 : {Shop.total}원")

'''
3. 다음 지시사항을 읽고 Hybrid 클래스를 구현하세요.

지시사항
1. 다음과 같은 슈퍼 클래스 Car를 가지고 있는 Hybrid 클래스를 구현하세요.
2. 서브 클래스 Hybrid는 다음과 같은 특징을 가지고 있습니다.
    최대 배터리 충전량은 30입니다.
    배터리를 충전하는 charge() 메서드가 있습니다. 최대 충전량을 초과하도록 충전할 수 없고,
    0보다 작은 값으로 충전할 수 없습니다.
    현재 주유량과 충전량을 모두 확인할 수 있는 hybrid_info() 메서드가 있습니다.
    
3. 다음과 같은 방식으로 전체 동작을 확인할 수 있습니다.
car = Hybrid(oil=0, amount=0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()       # 현재 주유 상태 : 50 # 현재 충전상태 : 30
'''
class Car:
    max_oil = 50            # 최대 주유량
    def __init__(self, oil):
        self.oil = oil
    def add_oil(self, oil):
        if oil <= 0:
            return          # 메서드 정의 후에 return 후 아무 값도 쓰지 않는 것은 메서드를 종료하겠다는 의미
        self.oil += oil
        if self.oil > Car.max_oil:      # 주유 후 최대 주유량 초과 상태이면
            self.oil = Car.max_oil      # 현재 주유량을 최대 주유량으로 설정
    def car_info(self):
        print(f"현재 주유 상태 : {self.oil}")


class Hybrid(Car):
    max_amount = 30

    def __init__(self, oil, amount):
        super().__init__(oil)
        self.amount = amount

    def charge(self, amount):
        if amount <= 0:
            return  # 메서드 정의 후에 return 후 아무 값도 쓰지 않는 것은 메서드를 종료하겠다는 의미
        self.amount += amount
        if self.amount > Hybrid.max_amount:  # 주유 후 최대 충전량 초과 상태이면
            self.amount = Hybrid.max_amount  # 현재 충전량을 최대 충전량으로 설정


    def hybrid_info(self):
        # print(f"현재 주유 상태 : {self.oil}")
        print(f"현재 충전 상태 : {self.amount}")


car = Hybrid(oil=0, amount=0)
car.add_oil(100)        #
car.charge(50)
car.hybrid_info()       # 현재 주유 상태 : 50 # 현재 충전상태 : 30
car.car_info()