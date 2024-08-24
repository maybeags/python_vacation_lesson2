'''
p 292

1. 예외 처리의 필요성
    1. 예외와 오류
        예외 : 개발자가 직접 처리할 수 있는 문제
        오류 : 개발자가 처리할 수 없는 문제

    2. 예외 처리의 필요성
        예외 처리의 목적 : 어떤 문제가 발생했을 때 그 문제를 해결해 주는 것이 아니라,
        발생된 문제로 인해 프로그램이 비정상적으로 종료되는 것을 막고
        사용자에게 발생한 문제에 대한 정보를 전달하기 위함
'''

# 2 / 0

'''
Traceback (most recent call last):

    2 / 0
    ~~^~~
ZeroDivisionError: division by zero
Process finished with exit code 1
프로그램이 정상적으로 종료되지 않았음을 나타내는 자료로서, 예외로 처리할 수 있다면 비정상적인 종료를 막을 수 있다.

2 / 0
0으로 나눌 수 없습니다.

와 같은 방식으로 사전에 미리 준비하는 것이 예외 처리에 해당함.

2. 예외 처리
    1) 고전적인 예외 처리
'''
# a = int(input("제수를 입력 하세요 >>> "))           # 만약에 실수를 a에 입력했을 경우 string -> int 형변환이 일어나지 않기 때문에
#                                                 #   오류가 발생함. 이를 막기 위해 int(float(input("제수를 입력하세요 >>>)))
#                                                 # 와 같은 방식으로 코드를 작성하면 예외를 처리할 수 있음.
# b = int(input("피제수를 입력 하세요 >>> "))
# print(a)
#
# if b == 0:
#     print("0으로 나눌 수 없습니다.")
# else:
#     print(f"a / b = {a/b}")

'''
어떤 값이든 0으로 나눌 수 없기 때문에 if b == 0을 통해 0으로 나누는 것을 하지 못하도록 예외 처리를 함.

여기서 발생되는 문제는 :
    1. 어떤 문제가 발생할지 예상할 수 있어야 대비할 수 있다.
    2. 어떤 문제가 발생할지 예상하더라도 대비할 수 없는 경우가 있다.
    
2. 예외의 종류
+------+---------------------+---------------------------------------------+
| 순번 |     예외 클래스     |                     의미                    |
+------+---------------------+---------------------------------------------+
|  1   |    BaseException    |              최상위 예외 클래스             |
|  2   |      Exception      |       대부분 예외 클래스의 슈퍼 클래스      |
|  3   |   ArithmeticError   |          산술 연산에 문제가 있을 때         |
|  4   |    AttributeError   |           잘못된 속성을 참조할 때           |
|  5   |       EOFError      | 파일에서 더 이상 읽어 들일 데이터가 없을 때 |
|  6   | ModuleNotFoundError |           import할 모듈이 없을 때           |
|  7   |  FileNotFoundError  |           존재하지 않는 파일일 때           |
|  8   |      IndexError     |          잘못된 인덱스를 사용할 때          |
|  9   |      NameError      |        잘못된 이름(변수)을 사용할 때        |
|  10  |     SyntaxError     |               문법이 틀렸을 때              |
|  11  |      TypeError      |   계산하려는 데이터의 유형이 잘못되었을 때  |
|  12  |      ValueError     |    계산하려는 데이터의 값이 잘못되었을 때   |
+------+---------------------+---------------------------------------------+

3. 예외 처리 방식
    1) 모든 예외를 처리하는 방식 -> try / except문
    
    형식
    
try:
    코드 작성 영역
except:
    예외 발생 시 처리 영역
    
기본 예제

다음은 사용자가 입력한 키를 정수로 반올림해서 다시 저장하는 프로그램입니다. try/except문을 사용하여
'예외가 발생하였습니다.'를 출력할 수 있도록 작성하세요.
'''
# try:
#     height = input("키를 입력하세요 >>> ")
#     height = round(height)
#     print(f"입력하신 키는 {height}cm로 처리됩니다.")
# except:
#     print("예외가 발생하였습니다.")
'''
위의 코드를 실행하면 오류가 뜨는데, 이를 디버깅하지말고 예외처리하시오.

    2) 특정 예외만 처리하는 방식
        try / except문을 사용하면 기본적으로 예외의 종류에 상관없이 모든 예외가 처리됨.
        하지만 위에서 확인한 것처럼 0으로 나누는 경우와, 정수가 아닌 값을 입력한 경우에 서로 다른 메시지를 출력하는 방식이 있음.
        
        2)-1. 0으로 나누려고 하는 경우 -> 0으로 나눌 수 없습니다.
        2)-2. 정수가 아닌 값을 입력한 경우 -> 정수만 입력할 수 있습니다.
        해당 경우 except문 뒤에 처리하고자 하는 예외를 모두 명시하면 됩니다.
'''
# try:
#     a = int(input("제수를 입력 하세요 >>> "))
#     b = int(input("피제수를 입력 하세요 >>> "))
#     print(f"a / b = {a/b}")
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except ValueError:
#     print("정수만 입력할 수 있습니다.")
'''
거의 모든 예외는 Exception 클래스의 서브 클래스입니다. 따라서 모든 예외는 Exception의 인스턴스가 됩니다.
다음과 같이 마지막에 작성하는 except문에 Exception을 명시하면 예상하지 못한 예외들도 모두 처리할 수 있습니다.

형식 :

try:
    코드 작성 영역
except 예외 클래스1:
    예외 메시지1
except 예외 클래스2:
    예외 메시지2
.
.
.
except Exception:
    예외 메시지
    
3. 예외 메시지 처리하기

지금까지는 직접 예외 메시지를 만들어서 사용했지만, 기본적으로 예외 메시지를 이미 가지고 있는 경우가 있습니다.
디폴트 에러 메시지를 출력하는 방식에 대해서 학습합니다.

형식 :

try:
    코드 작성 영역
except 예외 as 예외 메시지:
    예외 발생 시 처리 영역
'''
# z = [10, 20, 30, 40, 50]
# try:
#     z[10]
# except IndexError as e:
#     print(e)
'''
4. else문 finally문

try / except 문에 추가로 else문과 finally문을 사용할 수 있음.
else문을 예외가 발생하지 않으면 처리되는 구문
finally문은 예외 발생과 상관없이 항상 처리되는 구문

형식 :

try:
    코드 작성 영역
except:
    예외 발생 시 처리 영역
else:
    예외가 없을 시 처리 영역
finally:
    언제나 실행되는 영역
'''
# try:
#     a = int(input("제수를 입력하세요 >>> "))
#     b = int(input("피제수를 입력하세요 >>> "))
#     result = a / b
# except ZeroDivisionError as e:
#     print(e)
# except ValueError:
#     print("정수만 입력할 수 있습니다.")
# else:
#     print(f"a / b = {result}")
# finally:
#     print("프로그램이 종료됩니다.")
'''
4. 강제로 예외 발생시키기

어떤 사람의 나이를 정수로 입력 받는 프로그램이 있다고 가정했을 때,
컴퓨터 상으로는(그리고 파이썬 상에서는) -1000이 정수이기 때문에 예외가 발생하지 않습니다.
하지만, -1000살이 될 수 없기 때문에 직접 예외를 만들어서 처리해야 함. -> raise문 사용

형식 :

raise 예외클래스()

또는

raise 예외클래스(예외메시지)

raise는 강제로 예외를 발생시킨다는 의미로, 이때 주로 사용되는 예외 클래스는 Exception입니다.
'''
# age = int(input("나이를 입력하세요 >>> "))            # 파이썬 상 문제가 없지만 현실 세계에서 생기는 예외 -> 직접 처리할 필요가 있음
# print(f"당신의 나이는 {age}살입니다.")

# try:
#     raise Exception("강제로 발생시킨 예외")
# except Exception as e:
#     print("발생한 예외 메시지는 다음과 같습니다.")
#     print(e)

'''
    raise문은 try문 내부에 작성함. 실제 프로그램을 구현할 때는 if문을 이용해서 예외를 발생시켜야 하는 조건문을 먼저
    작성한 뒤, raise문을 작성하는 것이 일반적.
5. 사용자 정의 예외 클래스
'''
# 음수를 입력받았을 때 강제로 예외를 발생시키기 위한 예외 클래스 정의
# class NegativeAgeError(Exception):
#     """사용자 정의 예외 클래스: 나이가 음수일 때 발생"""
#     pass        # 예외를 발생시키기만 하면 되기 때문에 따로 코드 작성할 필요가 없음 -> Exception의 속성 및 메서드를 상속
#
# try:
#     age = int(input("나이를 입력하세요 >>> "))
#     if age < 0:
#         raise NegativeAgeError("나이는 음수일 수 없습니다.")
# except NegativeAgeError as e:
#     print("발생한 예외 메시지는 다음과 같습니다.")
#     print(e)
# except ValueError:
#     print("정수만 입력 가능합니다.")
# else:
#     print(f"입력한 나이 : {age}")
# finally:
#     print("프로그램을 종료합니다.")
'''
기본 예제

사용자의 점수를 0부터 100 사이로 입력받아서 점수가 80점 이상이면 합격, 아니면 불합격을 출력하는 프로그램입니다.
입력된 점수가 0~100 사이의 유효한 값이 아니라면 예외를 발생시키고 '점수는 0~100 사이입니다.'라는 예외 메시지를 출력합니다.
# '''
# try:
#     score = float(input("점수를 입력하세요 >>> "))
#     if score < 0 or score > 100:
#         raise Exception("점수는 0~100 사이입니다.")
# except ValueError:
#     print("점수는 숫자여야 합니다.")
# except Exception as e:
#     print(e)
# else:
#     if score >= 80:
#         print("합격")
#     else:
#         print("불합격")
# finally:
#     print("프로그램을 종료합니다.")


'''
과제 1 : 기본적인 예외 처리
사용자로부터 숫자를 입력 받아 해당 숫자를 100을 해당 숫자로 나누는 값을 출력하는 프로그램을 작성하시오.
만약 사용자가 0을 입력하거나 숫자가 아닌 값을 입력하면 적절한 예외 메시지를 출력하시오.

지시 사항.

1. 사용자로부터 숫자를 입력 받는다.
2. 입력받은 숫자를 100을 해당 숫자로 나누어 결과를 출력한다.
3. 입력값이 0일 경우, ZeroDivisionError를 처리하여 "0으로 나눌 수 없습니다."라는 메시지를 출력한다.
4. 입력값이 숫자가 아닌 경우, ValueError를 처리하여 "숫자만 입력할 수 있습니다."라는 메시지를 출력한다.
5. 예외가 발생하지 않는 경우, "정상적으로 처리되었습니다."라는 메시지를 출력한다.
6. 프로그램 종료 메시지를 출력한다.
'''
# try:
#     num = float(input("숫자를 입력하세요 >>> "))
#     result = 100 / num
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except ValueError:
#     print("숫자만 입력할 수 있습니다.")
# except Exception:
#     print("예상할 수 없는 오류가 발생했습니다.")
# else:
#     print("정상적으로 처리되었습니다.")
#     print(f"결과 : {result}")
# finally:
#     print("프로그램이 종료되었습니다.")

'''
과제 2: 리스트 인덱스 예외 처리

사용자로부터 리스트의 인덱스를 입력 받아 해당 인덱스의 값을 출력하는 프로그램을 작성하시오.
만약 잘못된 인덱스를 입력하면 적절한 예외 메시지를 출력하시오.

지시 사항
1. 미리 정의된 리스트가 있다.
2. 사용자로부터 리스트의 인덱스를 입력 받는다.
3. 입력받은 인덱스를 사용하여 리스트의 값을 출력한다.
4. 인덱스가 리스트의 범위를 벗어나면 적절한 메시지를 출력한다.
5. 입력값이 숫자가 아니면 적절한 메시지를 출력한다.
6. 예외가 발생하지 않은 경우 "정상적으로 처리되었습니다."라는 메시지를 출력한다.
7. 프로그램 종료 메시지를 출력한다.
'''
class NegativeNumIndexError(Exception):
    pass
# class OverIndexError(Exception):
#     pass
#
# my_list = [10, 20, 30, 40, 50]
#
# try:
#     index = int(input("리스트의 인덱스를 입력하세요 >>> "))
#
#     if index < 0:
#         raise NegativeNumIndexError("음수는 입력할 수 없습니다.")
#     print(f"리스트의 값 : {my_list[index]}")
#     # if index > 4:
#     #     raise OverIndexError("인덱스의 범위를 넘어섰습니다.")
# except NegativeNumIndexError as e:
#     print("발생한 예외 메시지는 다음과 같습니다.")
#     print(e)
# # except OverIndexError as e:
# #     print("발생한 예외 메시지는 다음과 같습니다.")
# #     print(e)
# except IndexError:
#     print("잘못된 인덱스입니다.")
# except ValueError:
#     print("0과 자연수만 입력할 수 있습니다.")
# except Exception:
#     print("예상할 수 없는 오류가 발생했습니다.")
# else:
#     print("정상적으로 처리되었습니다.")
# finally:
#     print("프로그램이 종료되었습니다.")

'''
과제 3 : 속성 참조 예외 처리
사용자로부터 속성명을 입력받아 객체의 해당 속성을 출력하는 프로그램을 작성하시오.
만약 잘못된 속성을 입력하면 적절한 예외 메시지를 출력하시오.

지시사항
1. 미리 정의된 클래스와 객체가 있다.
2. 사용자로부터 속성명을 입력 받는다.
3. 입력받은 속성명을 사용하여 객체의 속성을 출력한다.
4. 잘못된 속성을 입력하면 "존재하지 않는 속성입니다."라는 메시지를 출력한다.
5. 예외가 발생하지 않은 경우, "정상적으로 처리되었습니다."라는 메시지를 출력한다.
6. 프로그램 종료 메시지를 출력한다.
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person(name="John", age=30)
try:
    attribute = input("출력할 속성명을 입력하세요 >>> ")
    print(f"{getattr(person, attribute)}")
except AttributeError:
    print("존재하지 않는 속성입니다.")
else:
    print("정상적으로 처리되었습니다.")
finally:
    print("프로그램이 종료되었습니다.")


# index = int(input("리스트의 인덱스를 입력하세요 >>> "))
# print(my_list[index])

# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.field_names = ["순번", "예외 클래스", "의미"]
# table.add_row([1, "BaseException", "최상위 예외 클래스"])
# table.add_row([2, "Exception", "대부분 예외 클래스의 슈퍼 클래스"])
# table.add_row([3, "ArithmeticError", "산술 연산에 문제가 있을 때"])
# table.add_row([4, "AttributeError", "잘못된 속성을 참조할 때"])
# table.add_row([5, "EOFError", "파일에서 더 이상 읽어 들일 데이터가 없을 때"])
# table.add_row([6, "ModuleNotFoundError", "import할 모듈이 없을 때"])
# table.add_row([7, "FileNotFoundError", "존재하지 않는 파일일 때"])
# table.add_row([8, "IndexError", "잘못된 인덱스를 사용할 때"])
# table.add_row([9, "NameError", "잘못된 이름(변수)을 사용할 때"])
# table.add_row([10, "SyntaxError", "문법이 틀렸을 때"])
# table.add_row([11, "TypeError", "계산하려는 데이터의 유형이 잘못되었을 때"])
# table.add_row([12, "ValueError", "계산하려는 데이터의 값이 잘못되었을 때"])
