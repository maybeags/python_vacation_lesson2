# 클래스 선언 방법 : class 클래스명(대문자로시작):

# 클래스 : 객체 지향 프로그래밍에서 객체를 생성하기 위한 청사진(설계도), 또는 틀을 의미.
#       클래스 내부에는 데이터(속성)와 이 데이터에 작용하는 함수(메서드)를 묶어서 하나로 관리함.
class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0

        # 위의 것들이 속성(attributes)
        # 속성 : 클래스 내의 변수를 의미, 객체의 '상태', 즉 User의 클래스의 속성 id, username, followers, following이 있다.

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def set_username(self, new_username):
        self.username = new_username

    def get_username(self):
        return self.username

        # 위의 follow()가 메서드에 해당하고, 클래스가 수행하는 동작, 객체의 '행동'을 정의하는 함수


# 객체 생성
user_1 = User("001", "ahn")
user_2 = User("002", "soo")

#메서드 호출
user_1.follow(user_2)
# print(user_1.following)
# print(user_1.followers)
print(user_1.username)
user_1.username = "kim"            # 객체의 속성에 직접 접근하여 데이터를 바꾼 사례 -> 보안에 취약
print(user_1.get_username())
user_1.set_username("park")        # 객체 속성을 메서드를 경유하여 데이터를 바꾼 사례 -> 보완성이 있고 다양한 중간 과정을 거칠 수 있음
print(user_1.get_username())



'''
클래스의 주요 개념
    1. 캡슐화(Encapulation) : 객체의 속성과 메서드를 하나로 묶고, 일부를 외부에 감추어 은닉하는 것.
    2. 상속(Inheritance) : 하나의 클래스가 다른 클래스의 속성과 메서드를 상속받아 사용하는 것. 코드의 재사용성을 높이고, 계층적 관계 형성
    3. 다형성(Polymorphism) : 동일한 인터페이스를 통해 서로 다른 구현을 제공하는 것. 다양한 객체가 동일한 메시지에 대해 각기 다른 방식
        으로 응답할 수 있게 해줌.
'''


