'''
p 116

for 문 : 값의 범위나 횟수가 정해져 있을 때 사용하면 편리한 반복문 -> while은 범위나 횟수를 모를 때 사용 가능하기 때문에
어떤 때에 for / while을 쓸지 고민할 필요가 있음.

형식 :
for 변수 in 반복가능객체:
    반복실행문

* 반복가능객체(iterable) : 반복해서 사용할 수 있는 객체. 객체 내부에 요소가 여러 개 저장되어 있고 한 번에 하나씩 꺼내서
사용할 수 있는 객체를 의미함. str, list, tuple, set, dict가 해당되며, str만 수업했으며 나머지는 collection개념이므로 추후
수업 예정
'''

'''
p 119

for문과 문자열
for 문자 in 문자열:
    반복실행문
'''

# str_example = "Hello"
# print(str_example[0])
# print(str_example[1])
# print(str_example[2])
# print(str_example[3])
# print(str_example[4])
#
# for n in str_example:
#     print(n)

# for v in "nice":
#     print(v)
'''
p 123

for문과 range()함수
range() 함수는 정수 범위를 만들어 낼 때 사용하는 함수, 특히 for문과 range() 함수를 사용하면 개발자가 원하는 범위의 값을
쉽게 생성할 수 있습니다.

형식 :
range(초깃값, 종료값, 증감값)
1. 초깃값부터 종료값 '이전'까지의 숫자(n)들의 컬렉션을 만듭니다.
    (초깃값 <= n < 종료값)
2. 초깃값을 생략하면 0부터 시작합니다.
3. 종료값은 생략할 수 없습니다.
4. 증감값을 생략하면 1씩 증가합니다.
'''
#
# for n in range(6):
#     print(n)

for n in range(2, 11):
    print(n)

'''
기본 예제

출력하고자 하는 구구단을 입력 받아 해당 구구단을 출력하는 프로그램을 작성하세요.
실행 예시
출력할 구구단을 입력하세요 >>> 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45

https://m.site.naver.com/1pUhP
'''

dan = int(input("출력할 구구단을 입력하세요 >>> "))
for n in range(1, 10):
    print(f"{dan} x {n} = {dan*n}")

'''
huddle3

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():    
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()


'''