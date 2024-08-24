'''
p 39

컬렉션(collection) : 여러 값을 하나의 이름으로 묶어서 관리하는 자료형

string의 경우 문자 하나하나를 줄(string)로 묶어서 문자열로 출력하는데, 예를 들어
'다수의 다른 string을 관리하는 방법은 무엇일까?'에 대한 대답

여러 명의 프로필을 관리한다고 가정했을 때,
'''

#ahn_geunsu = "이름 : 안근수\n나이 : 37\n직업 : 코리아it아카데미 파이썬 강사"
#print(ahn_geunsu)
#park_minji = "이름 : 박민지\n나이 : 17\n직업 : 코리아it아카데미 파이썬 학생"
'''
에 한 명 저장하는 것은 아무 문제가 없을 수 있지만 매번 변수 하나에 이름, 나이, 직업, 주소 등을 한 명 추가할 때 마다
정리하는 것은 비효율적이고, 예를 들어 ahn_geunsu에서 직업만 조회하고 싶어도 전체 정보를 확인해야만 합니다.
이를 한꺼번에 관리하기 위한 방식으로 모음(collection)을 사용 합니다.

종류
    1. list() - 추가, 수정, 삭제가 언제나 가능 / a = [1, 2, 3] # 대괄호
    2. tuple() - 추가, 수정, 삭제가 불가능 / a = (1, 2, 3) # 소괄호
    3. set() - 중복된 값의 저장 불가능 / a = {1, 2, 3} # 중괄호
    4. dict() - 키 + 값으로 관리 / a = {'age': 25}
    
이 중, 1, 2번인 list와 tuple은 저장된 값의 순서가 있는데 이를 시퀀스(sequence)라고 부릅니다.
즉, list는 저장 순서가 있고 추가, 수정, 삭제가 자유로우며, tuple의 경우 저장된 순서가 있으나 추가, 수정, 삭제가 불가능합니다.
'''

'''
1. list
    여러 값을 저장할 때 가장 많이 사용. 자료형이 서로 다르더라도 하나의 리스트에 저장 가능.
    하나의 배열(파이썬의 리스트와 비슷한 개념의 구조)에 하나의 자료형만을 저장할 수 있는 자료형만을 저장할 수 있는
    C나 JAVA에 비해 파이썬이 가지는 장점 중 하나라 할 수 있음.
'''
# li = [3, 4, 5]
# print(li)

'''
    1-1. list의 index와 slicing
    list는 str과 동일한 방식의 index와 slicing을 지원합니다.
    1-1-1. 인덱스 및 마이너스 인덱스
'''
# print(li[0])
# print(type(li))
# print(type(li[2]))
# print(li[-1])
# print(li[-2])
# print(li[-3])
# '''
#     1-1-2. 슬라이싱
# '''
# list_num1 = [100, 3.14, "hello"]        #리스트 생성 방법 1
# list_num2 = list([4, 5, 6, 7, 8, 9])    #리스트 생성 방법 2
# print(list_num2[0:5:2])

'''
    str의 슬라이싱과 같이 시작점 : 종료점 : 증감값으로 이루어져있음을 확인할 수 있다 -> 교재에 없습니다. 필기해두세요.
    1-1-2. 리스트 요소의 추가와 삭제
    
    리스트에 새로운 요소를 추가할 때는 append()와 insert() '메서드'를 사용할 수 있습니다. 기존 요소를 삭제할 때는 pop() 
    메서드를 사용합니다.
    
    append() - 항상 마지막 요소에 추가하는 메서드
    insert(위치, 값)
'''
# scores = [ 50, 40, 30 ]
# scores.append(100)
# print(scores)
# scores.insert(0, 90)
# print(scores)
'''
    pop()의 경우 빈 괄호로 사용하게 되면 맨 마지막 요소가 삭제됩니다.
    pop(위치)로 작성하면 해당 인덱스의 요소를 삭제합니다.
'''
# scores.pop()
# print(scores)
# scores.pop(0)
# print(scores)
# '''
#     2. tuple : 저장된 값을 변경할 수 없는 리스트라고 생각하시면 됩니다. 인덱스와 슬라이스를 사용하지만 저장된 값 이외에는
#     추가, 수정, 삭제가 불가능합니다.
#
#     튜플은 소괄호를 이용해 생성합니다.
# '''
# tuple_num1 = (1, 2, 3)          # 튜플 생성 방법 1
# print(tuple_num1)
# tuple_num2 = tuple((4, 5, 6))   # 튜플 생성 방법 2
# '''
# 하지만, tuple_num1 = 1, 2, 3과 같이 생성 가능합니다.
# '''
# a, b = 1, 2
# # name, age = input("이름을 입력하세요 >>> "), int(input("나이를 입력하세요 >>> "))
# tuple_num3 = 7, 8, 9           # 튜플 생성 방법 3
# print(type(a))
# print(b)
# # print(tuple_num2)
# print(tuple_num3)
'''
    튜플 생성 방법 3을 이용한다고 가정할 때, 값이 하나 뿐인 튜플을 생성한다면
    tuple_num4 = 7이라고 입력할 경우 생기는 문제점?
'''
# tuple_num4 = 7
# print(type(tuple_num4))
# tuple_num4 = 7,
# print(type(tuple_num4))

'''
시퀀스이기 때문에 인덱스 및 슬라이싱 사용 가능
'''
# print(tuple_num3[1])
# print(type(tuple_num3[2]))
# print(tuple_num3[1:3:2])
'''
3. set : 수학의 집합 개념을 구현한 자료형입니다. 리스트와의 차이점은 순서가 없기 때문에 인덱스 및 슬라이싱 사용이 불가능.
중복된 값의 저장을 사용하는 것이 불가능.
이를 활용하여 중복 제거용으로 사용하는 경우, 교집합, 합집합, 차집합과 같은 집합 개념이 필요한 경우 사용 가능.
'''

# set를 생성하기 위해서는 중괄호({})를 사용합니다.
#
# set_num1 = {1, 2, 3}        # 세트 생성 방법 1
# set_num2 = set( {4, 5, 6} )   # 세트 생성 방법 2
# print(set_num1)
# print(set_num2)
# li = []
# tu = ()
# se = {}
# print(type(se))
# # 비어있는 set를 만드는 방법은 세트 생성 방법 2를 이용해야만 한다.
# set_empty = set()
# print(type(set_empty))
'''
비어있는 세트를 생성할 때는 중괄호 사용 불가, s = {}와 같이 입력할 경우 세트 대신 빈 딕셔너리가 생성됩니다.
그래서 빈 세트를 생성할 경우에는 set() 함수를 사용해야만 합니다.

    3-2 특징
        3-2-1. 저장되는 순서가 없다 -> 인덱스 / 슬라이싱 불가능
        3-2-2. 중복되는 값을 저장할 수 없다.
        특히, 3-2-2의 특징으로 인해 세트는 단독으로 쓰이기 보다는 list와 연계하여 많이 사용 됩니다.
'''
# list_num4 = [1, 1, 2, 2, 3, 3]
# print(list_num4)
# set_num4 = set(list_num4)
# print(set_num4)                 # {1,2,3}으로 나오긴 했지만 순서가 있는 것은 아니다
# print(type(list(set_num4)))
'''
set에는 index / slice를 지원하지 않기 때문에 특정 요소만 추출하기 위해서는 list로 형변환하는 과정이 필요합니다.

    3-3. 세트 요소의 추가와 삭제
    세트에 새로운 요소를 추가할 때 - add()
    기존 요소를 삭제할 때 - remove() / discard()
'''
# set_num5 = {10, 20, 30}
# set_num5.add(50)
# print(set_num5) # set에는 순서가 없기 때문에 출력 결과가 순서대로 나오지 않을 수 있음.
# set_num5.remove(50) # 순서가 없기 때문에 '값'을 입력해야합니다.
# print(set_num5)
# set_num5.discard(20)
# print(set_num5)
# set_num5.discard(40)    #discard()는 set를 탐색하면서 해당 값이 없어도 오류가 발생하지 않습니다.
# print(set_num5)
# set_num5.remove(40)     #remove()는 값이 정확하지 않으면 KeyError가 발생합니다.
# print(set_num5)
'''
4. 딕셔너리 - 말 그대로 사전의 의미를 생각하시면 됩니다. 종이 사전을 펴보게 되면
flower: 꽃
dictionary: 사전
등으로 기록돼있습니다. 즉 : 을 기준으로 좌측과 우측이 나뉘어진 형태를 가지고 있는데, 딕셔너리는 이전의
리스트, 튜플, 세트와 달리 key: value의 구성으로 이루어져있습니다.
'''
dict_num1 = {
    "이름": "안근수",
    "나이": 37,
    "주소": "부산광역시 연제구"
}
'''
와 같은 방식으로 생성합니다.
'''
print(dict_num1)
print(dict_num1["이름"])
'''
딕셔너리는 인덱스는 존재하지 않지만 위와 같이 key를 인덱스로 사용합니다. 
즉, 키값(key)을 알면 저장된 값(value)을 확인할 수 있는 구조.
'''
print(dict_num1.keys())     # 딕셔너리.keys() 메서드   -> key 목록
print(dict_num1.values())   # 딕셔너리.values() 메서드 -> value 목록
'''
    4-1. 딕셔너리 요소의 추가와 삭제
'''
dict_num1["직업"] = "코리아it아카데미 파이썬 강사"
print(dict_num1)
# 기존에 없었던 key를 입력하고 = 뒤에 value를 입력하시면 됩니다. 하나의 키에 서로 다른 값을 저장할 수 없습니다.
dict_num1["직업"] = "영어 과외 강사"    # 딕셔너리 수정 방법
print(dict_num1)
dict_num1.pop("직업")
print(dict_num1)

'''
응용 예제
어떤 중국음식점의 이번 주말 할인 메뉴는 금요일은 탕수육, 토요일은 유산슬, 일요일은 팔보채입니다.
요일별 할인 메뉴를 딕셔너리(dict)구조로 저장하고 다음과 같이 출력하는 프로그램을 구현하세요.

실행 예
금요일 : 탕수육
토요일 : 유산슬
일요일 : 팔보채

for문과 dictionary를 이용하는 방법이 있지만 아직 조합 수업을 하지 않았습니다.
print()함수를 세 번 사용하여 출력하시면 됩니다.
'''
discount_menu = {
    "금요일": "탕수육",
    "토요일": "유산슬",
    "일요일": "팔보채"
}
print(f"금요일 : {discount_menu["금요일"]}")
print(f"토요일 : {discount_menu["토요일"]}")
print(f"일요일 : {discount_menu["일요일"]}")

'''
리스트 [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 ]의 3번째 요소부터 7번째 요소만 추출한 결과, 그 리스트에서 두 번째
요소를 출력하는 프로그램을 구현하세요.

실행 예
3번째 요소부터 7번째 요소 = [ 30, 40, 50, 60, 70 ]
3번째 요소부터 7번째 요소 중 2번째 요소 = 40
'''
list_original = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list_index = list_original[2:7]
print(f"3번째 요소부터 7번째 요소 = {list_index}")
second_index = list_index[1]
print(f"3번째 요소부터 7번째 요소 중 2번째 요소 = {second_index}")

'''
사용자로부터 1에서 12사이의 월을 입력받아 해당 월이 며칠까지 있는지 출력하는 프로그램을 구현하세요.

실행 예
1~12 사이의 월을 입력하세요 >>> 2
2월은 28일까지 있습니다.
'''
# date = [ 28, 30, 31 ]
# last_date = 0
# month = int(input("1~12 사이의 월을 입력하세요 >>> "))
# if month == 2:
#     print(f"{month}월은 {date[0]}일까지 있습니다.")
#     last_date = date[0]
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     last_date = date[1]
# elif month in (1, 3, 5, 7, 8, 10, 12):
#     last_date = date[2]
# else:
#     print("잘못입력하셨습니다.")
#
# print(f"{month}월은 {last_date}일까지입니다.")

#
# month_second = int(input("1~12 사이의 월을 입력하세요 >>> "))
# list_month = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
# print(f"{month_second}월은 {list_month[month_second -1]}일까지 있습니다.")
#
#
'''
수학여행을 어디로 갈지 결정하기 위해 학생들이 희망하는 모든 수학여행 장소를 조사하기로 했습니다.
학생들이 원하는 장소를 입력받아 동일한 입력을 무시하고 모든 입력을 저장하려고 합니다.
학생을 3명으로 가정하고 실행 예와 같이 동작하는 프로그램을 구현하세요.

실행 예
희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 민속촌

조사된 수학여행지는 {"제주", "민속촌}입니다.
'''
#
# field_trip = set()
# place = []
#
# student1 = input("희망하는 수학여행지를 입력하세요 >>> ")
# student2 = input("희망하는 수학여행지를 입력하세요 >>> ")
# student3 = input("희망하는 수학여행지를 입력하세요 >>> ")

# field_trip.add(student1)
# field_trip.add(student2)
# field_trip.add(student3)
#
# place.append(student1)
# place.append(student2)
# place.append(student3)
#
# set_place = set(place)
#
# print(f"조사된 수학여행지는 {set_place}입니다.")

'''
사용자로부터 임의의 양의 정수를 하나 입력받은 뒤 그 숫자만큼 '과일 이름'을 입력받아 
'basket' 리스트에 저장하는 프로그램을 구현하세요.

실행 예
몇 개의 과일을 보관할까요? >>> 5
1번째 과일을 입력하세요 >>> 사과
2번째 과일을 입력하세요 >>> 바나나
3번째 과일을 입력하세요 >>> 체리
4번째 과일을 입력하세요 >>> 오렌지
5번째 과일을 입력하세요 >>> 망고
입력받은 과일들은 ["사과", "바나나", "체리", "오렌지", "망고"]입니다.
'''
# count_num = int(input("몇 개의 과일을 보관할까요? >>> "))
# fruits = []
# for n in range(1, count_num+1):
#     fruit = input(f"{n}번째 과일을 입력하세요 >>> ")
#     fruits.append(fruit)
# print(f"입력받은 과일들은 {fruits}입니다.")

count_num = int(input("몇 개의 과일을 보관할까요? >>> "))
basket = []
i = 1
while i <= count_num:
    fruit = input(f"{i}번째 과일을 입력하세요 >>> ")
    basket.append(fruit)
    i += 1

print(f"입력받은 과일들은 {basket}입니다.")












