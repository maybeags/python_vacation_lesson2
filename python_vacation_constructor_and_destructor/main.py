'''
p 276

1. 생성자
'''

# class Candy:
#
#     def set_info(self, shape, color):
#         self.shape = shape
#         self.color = color
#
# satang = Candy()
# satang.set_info(shape="cicle", color="brown")
'''
satang = Candy() 코드가 실행되면서 satang 인스턴스(객체)가 생성됨.
이 때 satang 인스턴스에 저장된 모양과 색상 정보는 없음.
'''

# class Book:
#
#     def set_info(self, title, author):
#         self.title = title
#         self.author = author
#
#     def print_info(self):
#         print(f"책 제목 : {self.title}")
#         print(f"책 저자 : {self.author}")
#
#
# book1 = Book()
# book2 = Book()
#
# book1.set_info("파이썬", "민경태")
# book2.set_info("어린왕자", "생텍쥐페리")
#
# book1.print_info()
# book2.print_info()
'''
satang 인스턴스는 생성된 이후에 set_info() 메서드를 호출하여 circle 모양의 brown 색의 사탕이라는 값을 가지게 됨.

satang 인스턴스의 생성 과정 :
1. 값이 없는 인스턴스를 생성
2. 값을 저장할 수 있는 메서드를 호출

처음부터 값이 있는 인스턴스를 생성하기 위한 방법 : __init__() 메서드
__init__() 메서드(생성자)는 인스턴스가 생성될 때 자동으로 호출되기 때문에 인스턴스 변수의 초기화 용도로 사용,
값이 있는 인스턴스를 생성할 수 있다는 의미.
'''

# class Candy2:
#
#     def __init__(self, shape, color):
#         self.shape = shape
#         self.color = color
#
#
# satang2 = Candy2("정육면체", "흰색")

'''
santang 인스턴스와 satang2 인스턴스의 생성 방식에 주목할 것
'''
#
# class User:
#
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.followings = 0
#
#
# class Book2:
#
#     def __init__(self):
#         self.title = ""
#         self.author = ""

'''
이상에서 다양한 방식의 생성자 사용법에 대해서 학습함 -> 이전 수업 내용과 연계해서 확인해주세요.

2. 소멸자(destructor)

인스턴스가 생성될 때 자동으로 생성되는 생성자와 마찬가지로 인스턴스가 소멸될 때 자동으로 호출되는 메서드가 있음.
이를 소멸자라고 하며 소멸자는 __del__()
'''

# class Sample:
#
#     def __del__(self):
#         print("인스턴스가 소멸됩니다.")
#
#
#
# sample = Sample()
# del sample

'''
기본 예제

생성자를 이용해서 용량을 가진 usb 인스턴스를 만드는 프로그램을 구현하시오.


1. 클래스 USB를 만드시오.
2. __init__을 정의하여 매개변수로 capacity를 받고, info()메서드를 정의하시오.

usb = USB(64)
usb.info()

실행 예
64GB USB
'''

class USB:

    def __init__(self, capacity):
        self.capacity = capacity

    def info(self):
        print(f"{self.capacity}GB USB")


usb = USB(64)
usb.info()

'''
생성자와 소멸자를 이용하여 서비스 안내 메시지를 출력하는 프로그램을 작성하시오.

class Service를 정의하고, 생성자를 통해 매개변수로 service를 받고, print()문을 쓰시오.
소멸자를 정의하여 Service가 종료됐음을 안내 하시오.


s = Service("길 안내")
del s

실행 예
길 안내 Service가 시작되었습니다.
길 안내 Service가 종료되었습니다.

'''
class Service:

    def __init__(self, service):
        self.service = service
        print(f"{self.service} Service가 시작되었습니다.")

#    def __del__(self):
#        print(f"{self.service} Service가 종료되었습니다.")

s = Service(service="길 안내")
del s







