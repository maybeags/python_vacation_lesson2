'''
p 258

1. 클래스 도입의 필요성
'''
#
# def student_info(name, department, professor, phone, address, grade):
#     print(name)
#     print(department)
#     print(professor)
#     print(phone)
#     print(address)
#     print(grade)
#
#
# name1 = "emily"
# department1 = "computer science"
# professor1 = "james"
# phone1 = "010-1111-2222"
# address1 = "seoul"
# grade1 = "A"
# student_info(name1, department1, professor1, phone1, address1, grade1)

'''
지금까지 배운 함수와 매개변수, 인수를 통해 여섯 개의 변수를 잘 처리할 수 있습니다. 하지만
만들어야 할 변수의 개수가 너무 많고, 학생 1 명당 변수가 6개라면,
학생이 100명이면 600개의 변수를 처리할 필요가 있습니다.

그래서 한 명만 더 타이핑 해보겠습니다.
'''
#
# name2 = "alice"
# department2 = "chemical science"
# professor2 = "david"
# phone2 = "010-3333-444"
# address2 = "busan"
# grade2 = "B"
#
# student_info(name2, department2, professor2, phone2, address2, grade2)

'''
해당 방식을 이용하면 학생 1명 추가할 때마다 변수가 6개씩 늘어나는 상황이 생깁니다.

이런 상황을 벗어나기 위해 클래스와 객체를 이용할 수 있습니다.
'''
'''
p 260

클래스의 개념
클래스란? 객체를 만드는 도구 -> 청사진 / 설계도 / 틀 등으로 비유됨.
하나의 클래스를 통해 여러 가지 객체를 만들 수 있다.

자동차 설계도 -> 클래스
설계도를 통해 생성된 자동차들 -> 객체

같은 설계도로 만든 자동차라 하더라도 서로 다른 옵션을 가질 수 있습니다.
마찬가지로 같은 클래스로 만든 객체라 하더라도 객체들은 서로 다른 값을 가질 수 있습니다.

인스턴스(instance) 역시 클래스를 이용해서 생성한 객체를 가리키는 용어입니다.
객체와 인스턴스는 그 둘을 바라보는 관점의 차이로 볼 수 있습니다.

1. 자동차 설계도 클래스로 만든 자동차는 객체(object)입니다.
2. 자동차는 자동차 설계도 클래스의 인스턴스(instance)입니다.
'''
'''
p 261

클래스 정의

클래스를 작성하는 것을 클래스 정의 -> 함수 정의와 비슷

형식 :

class 클래스명:
    본문
----------------------------------------------    
객체생성형식 :

객체이름 = 클래스명()       tim = Turtle()
'''
# class WaffleMachine:            # 클래스명은 대문자로 시작하는 camel case 카멜표기법
#     pass                        # 나중에 코드를 작성하겠다는 의미로 이 경우 실행시켜도 오류가 나지 않음
#
# waffle = WaffleMachine()        # 객체 생성
# print(waffle)
# print(waffle)을 실행시켰을 때, object라고 표기된 점을 미루어 WaffleMachine의 객체임을 확인할 수 있음.

'''
p 264

클래스의 구성

1. 클래스의 기본 구성
    객체를 만들어내는 클래스는 객체가 가져야 할 구성요소를 지니고 있습니다. 
    객체를 생성하기 위해 클래스는 객체가 가져야 할 '값'과 '기능'을 가지고 있어야 합니다.
    
    값 = 속성(attributes)
    기능 = 메서드(methods)
    
    클래스를 구성하는 변수는 두 가지로 분리됩니다. 클래스를 기반으로 생성된 모든 인스턴스들이 공유하는 변수인 클래스 변수와
    모든 인스턴스들이 개별적으로 가지는 변수인 인스턴스 변수 입니다.
    
    메서드는 특징에 따라서,
    클래스 메서드, 정적 메서드, 인스턴스 메서드로 분리 가능합니다.
    
    인스턴스 변수 : 클래스를 기반으로 만들어지는 모든 인스턴스들이 각각 따로 저장하는 변수를 의미
    모든 인스턴스 변수는 self라는 키워드를 앞에 붙여줍니다. 인스턴스 메서드는 인스턴스 변수를 사용하는 메서드
    인스턴스 변수값에 따라서 각 인스턴스(객체)마다 다르게 동작합니다.
    인스턴스 메서드는 첫번째 매개변수로 self를 추가해야합니다.
    
    인스턴스 변수와 인스턴스 메서드는 객체지향프로그래밍(oop)에서 중요한 개념입니다.
    이 두 가지는 클래스와 객체의 '상태'와 '동작'을 정의하는 데 사용됩니다.
    상태 = 속성
    동작 = 메서드
    
    # 인스턴스 변수
    각 인스턴스(객체)마다 개별적으로 유지되는 변수. 객체가 생성될 때마다 새로 할당. 각 객체는 고유한 인스턴스 변수 값을 가질 수 있음.
    
       인스턴스 변수의 정의 :
            인스턴스 변수는 일반적으로 클래스의 생성자 메서드(__init__) 내에서 self 키워드를 사용하여 정의됩니다.
'''
# 클래스 정의
# class Pokemon:
#     # 생성자
#     def __init__(self, number, name, type):
#         self.number = number
#         self.name = name
#         self.type = type
#
#
# # 객체 생성
# pokemon1 = Pokemon(1, "이상해씨", "풀/독")
# pokemon2 = Pokemon(name="파이리", number=4, type="불꽃")       # keyword argument
'''
여기서 number, name, type이 인스턴수 변수에 해당함. 즉 각 Pokemon 객체는 독립적인 인스턴스 변수 값을 지님.

    # 인스턴스 메서드
        인스턴스 메서드는 클래스의 각 인스턴스에서 호출될 수 있는 메서드. 주로 객체의 동작을 정의함.
        인스턴스 메서드는 첫 번째 매개변수로 항상 self를 받아야 하며, 이를 통해 해당 메서드가 호출된 객체에 접근할 수 있음.
'''

# class Pokemon:
#     # 생성자
#     def __init__(self, number, name, type):
#         self.number = number
#         self.name = name
#         self.type = type
#
#
#     def display_info(self):         #인스턴스 메서드
#         print(f"번호: {self.number}, 이름: {self.name}, 속성: {self.type}")
#
#
# # 객체 생성
# pokemon1 = Pokemon(1, "이상해씨", "풀/독")
# pokemon2 = Pokemon(name="파이리", number=4, type="불꽃")  # keyword argument
#
# # 인스턴스 메서드 호출
# pokemon1.display_info()
# pokemon2.display_info()
'''
이상의 display_info() 메서드는 인스턴스 메서드에 해당. 이 메서드는 객체의 인스턴스 변수에 접근하여 객체의 정보를 출력.

# 인스턴스 변수와 인스턴스 메서드의 관계

- 인스턴스 변수는 객체의 데이터를 저장합니다. 예를 들어, pokemon1 객체의 name 인스턴스 변수는 "이상해씨"라는 값을 가짐.
- 인스턴스 메서드는 이 데이터를 사용하여 동작을 수행합니다. 예를 들어 display_info() 메서드는 객체의 name 인스턴스 변수를 사용,
    해당 객체의 이름을 출력함.
- 인스턴스 메서드는 self 키워드를 사용하여 객체의 인스턴스 변수에 접근할 수 있음. 이를 통해 객체 내부의 데이터를 조작, 참조 가능.


'''
#
# pokemon2.name = "리자드";
# pokemon2.display_info()

class Person:

    def set_info(self, name, age, tel, address):        # init을 쓰지 않고도 가능
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address


boy = Person()
boy.set_info("안근수", 37, "010-7445-7113", "부산광역시 연제구")
print(boy.name)
print(boy.age)
print(boy.tel)
print(boy.address)













