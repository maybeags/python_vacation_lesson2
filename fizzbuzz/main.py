'''
FizzBuzz 게임 규칙"
1. 프로그램은 1부터 100까지의 숫자를 차례로 출력합니다.
2. 숫자가 3으로 나누어 떨어지면 숫자 대신 "Fizz"를 출력합니다.
3. 숫자가 5로 나누어 떨어지면 숫자 대신 "Buzz"를 출력합니다.
4. 숫자가 3과 5 모두로 나누어 떨어지면 숫자 대신 "FizzBuzz"를 출력합니다.
'''

for i in range(1, 101):     # 1부터 100까지의 숫자를 반복
    # if i % 15 == 0:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

        