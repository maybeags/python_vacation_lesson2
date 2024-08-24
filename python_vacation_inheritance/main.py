from prettytable import PrettyTable

# table = PrettyTable()
# table.field_names = [ "구분", "부모 클래스", "자식 클래스" ]
# table.add_row(["의미", "상속해주는 클래스", "상속받는 클래스"])
# table.add_row(["용어", "슈퍼 클래스", "서브 클래스"])
# table.add_row(["", "기반 클래스", "파생 클래스"])
# print(table)

'''
p 283

상속

1. 상속이란?
    어떤 클래스가 가지고 있는 기능을 그대로 물려받아서 사용할 수 있는 클래스를 생성할 수 있는데,
    클래스의 기능을 물려받을 때 상속받는다는 표현을 사용함.
    상속 관계에 있는 클래스를 표현할 때 부모 클래스 / 자식 클래스라는 용어를 사용함.
    
+------+-------------------+-----------------+
| 구분 |    부모 클래스    |   자식 클래스   |
+------+-------------------+-----------------+
| 의미 | 상속해주는 클래스 | 상속받는 클래스 |
| 용어 |    슈퍼 클래스    |   서브 클래스   |
| 용어 |    기반 클래스    |   파생 클래스   |
+------+-------------------+-----------------+
2. 상속 관계 구현
    두 클래스가 상속 관계에 놓이려면 IS-A 관계를 성립해야함. IS-A 관계란 "~은 ~이다"로 해석할 수 있는 관계를 의미 -> ex) "학생은 사람이다"
    
    *IS-A 원문 : is a kind of -> Dog is a kind of Animal -> '개'는 '동물'의 한 종류이다.
    
    형식:
class 슈퍼 클래스:
    본문

class 서브 클래스(슈퍼 클래스):
    본문    
'''
class Person:               # 슈퍼 클래스

    def __init__(self, name):       # 생성자
        self.name = name

    def eat(self, food):            # 메서드
        print(f"{self.name}이(가) {food}를 먹습니다.")


class Student(Person):      # 서브 클래스

    def __init__(self, name, school):
        super().__init__(name)      # name이라는 인스턴스 변수는 슈퍼 클래스로부터 상속 받는다는 의미
        self.school = school        # 슈퍼 클래스에는 없는 인스턴스 변수 school 선언 및 초기화

    def study(self):
        print(f"{self.name}는(은) {self.school}에서 공부를 합니다.")


potter = Student(name="해리포터", school="호그와트")
potter.eat("감자")                # 슈퍼 클래스의 메서드 호출
potter.study()                   # 자신 클래스의 메서드 호출

'''
3. 서브 클래스의 __init__()

서브 클래스는 슈퍼 클래스가 없으면 존재할 수 없습니다. 그러나 서브 클래스의 생성자를 구현하라 때는 
반드시 슈퍼 클래스의 생성자를 먼저 호출하는 코드를 작성해야만 합니다.

super -> 슈퍼 클래스를 의미. 즉, Student의 생성자를 호출하려면 super().__init__(name)에 의해서
슈퍼 클래스인 Person의 생성자가 먼저 호출되면서 슈퍼 클래스가 '생성'됩니다.
이후 슈퍼 클래스에서 생성된 인스턴스 변수인 name이 서브 클래스로 전달되고, 이후에 서브 클래스에서 school 인스턴스 변수를 정의하여
값을 저장하면서 생성됩니다.

4. 서브 클래스의 인스턴스 자료형

슈퍼 클래스의 객체는 슈퍼 클래스의 인스턴스
하지만 서브 클래스의 객체는 서브 클래스의 인스턴스이면서 동시에 슈퍼 클래스의 인스턴스
Student의 객체는 Student의 인스턴스이면서 동시에 Person의 인스턴스

어떤 객체가 어떤 클래스의 인스턴스인지 확인하기 위해서 사용하는 함수 -> isinstance()

형식 :

isinstance(객체, 클래스)
'''
print(isinstance(potter, Student))
print(isinstance(potter, Person))
'''
True / False를 반환함.
'''
















