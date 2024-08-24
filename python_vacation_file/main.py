'''
p 226

1. 파일 입출력의 개요
    파이썬을 이용하여 컴퓨터에 저장된 파일을 읽어 들이는 것과 새로운 파일을 생성해서 컴퓨터에 저장하는 것이 가능
    파일 입력(input) : 기존의 파일 내용을 읽어 들이는 것
    파일 출력(output) : 기존 파일에 새로운 내용을 추가하거나 새로운 파일을 생성하는 것

        1. 파일 열기
            실제로 어떤 파일을 열어본다는 의미가 X
            입출력 작업을 진행할 파일을 지정하는 것을 의미 -> 파일 입출력시 반드시 파일 열기 작업을 가장 먼저 수행해야함.

            open() 함수 사용
            형식 :

            파일 객체 = open(파일명, 모드)
            1) 파일명
                파일명은 입출력 작업을 수행할 파일을 의미.
                파일명만 작성할 수도 있고, 경로를 함께 작성할 수도 있음.
'''
import fileinput

# open("sample.txt")  # 파일명만 작성하는 경우 파이썬 소스 코드 파일과 같은 경로에 존재하는 파일
# open("C:/sample.txt") # 전체 경로를 작성하는 방법
# open("./sample.txt") # 현재 디렉토리(.)를 기준으로 경로 설정하는 방법
# open("../sample.txt") # 상위 디렉토리(..)를 기준으로 경로 설정하는 방법

'''
            2) 모드
                파일을 여는 목적 / 파일 입력을 위해서 혹은 출력을 위해서인지 모드를 통해서 결정함.
+------+------+-----------+-------------+---------------------+---------------------+
| 분류 | 종류 |    의미   |     설명    | 파일이 없을 때 동작 | 파일이 있을 때 동작 |
+------+------+-----------+-------------+---------------------+---------------------+
| 입력 |  r   |    read   |     읽기    |      오류 발생      |         읽기        |
| 출력 |  w   |   write   |     쓰기    |      새로 생성      |      새로 생성      |
|      |  a   |   append  |     추가    |      새로 생성      |         추가        |
|      |  x   | exclusive | 배타적 추가 |      새로 생성      |      오류 발생      |
+------+------+-----------+-------------+---------------------+---------------------+    
                입출력 모드를 생략하면 기본적으로 r 모드로 파일이 열립니다.
                w 모드나 a 모드와 같이 파일 출력을 목적으로 한다면 반드시 해당 모드를 명시해야 함.
                
                파일을 여는 목적을 결정하면, 어떤 파일인지 파일의 종류를 구분 해야합니다.
                일반적으로는 텍스트 파일인가 아닌가로 결정됩니다.    
+------+--------+-------------------------------------------+                
| 종류 |  의미  |                    설명                   |
+------+--------+-------------------------------------------+
|  t   |  text  |                텍스트 파일                |
|  b   | binary | 바이너리 파일(텍스트 파일 외의 모든 파일) |
+------+--------+-------------------------------------------+

        열고자 하는 파일의 종류를 생략하면 기본적으로 t 모드
        바이너리 파일의 경우에는 반드시 b 모드를 명시해야 함.
        
        종합하여 사용도 가능
+------+--------------------------------+
| 모드 |              설명              |
+------+--------------------------------+
|  rt  |     텍스트 파일 읽기 모드      |
|  rb  |    바이너리 파일 읽기 모드     |
|  wt  |     텍스트 파일 쓰기 모드      |
|  wb  |    바이너리 파일 쓰기 모드     |
|  at  |     텍스트 파일 추가 모드      |
|  ab  |    바이너리 파일 추가 모드     |
|  xt  |  텍스트 파일 배타적 추가 모드  |
|  xb  | 바이너리 파일 배타적 추가 모드 |
+------+--------------------------------+     

    2. 파일 닫기
        파일을 더 이상 사용하지 않거나 프로그램을 종료할 때 열어 놓은 파일을 닫는 편이 안전
        
    형식 :
    파일객체.close()            # 메서드로 되어있어 open()함수와 차이가 있음.
    
    3. 파일의 생성
'''

# file = open("myFile.txt", "wt") # myFile.txt 파일을 쓰기 모드로 open -> 파일이 없는 상태기 때문에 새로 생성
# print("myFile.txt 파일이 생성 되었습니다.")
# file.close()

'''
    4. with 문
        close() 메서드를 자동으로 호출할 수 있는 문법
    형식 :
        with open(파일명, 모드) as 파일객체:
            파일 처리 코드
'''
# with open("myFile.txt", "wt") as file:
#     print("myFile.txt 파일이 생성되었습니다.")
'''
2. 파일 출력(output)
    1. 텍스트 파일 생성하기
'''
#
# file = open("hello.txt", "wt")
#
# file.write("안녕하세요.\n반갑습니다.")
# '''
#     2. 텍스트 파일에 내용 추가하기
# '''
# file = open("hello.txt", "at")
# file.write("\nHello.\nNice to meet you.")
# print("hello.txt 파일에 새로운 내용이 추가되었습니다.")
# file.close()

'''
기본 예제

오늘의 스케줄을 입력하면 그 내용을 모두 파일에 보관하는 프로그램입니다.
스케줄을 입력하지 않고 enter를 누르면 프로그램은 종료됩니다.
생성되는 파일의 이름은 현재 날짜이고, 확장자는 txt입니다. "2020-10-22.txt"와 같은 형식을 갖추고 있습니다.
'''
#
# import time
#
# file = open(time.strftime("%Y-%m-%d")+".txt", "at")
# end_of_schedule = False
# while not end_of_schedule:
#     schedule = input("오늘의 스케줄을 입력하세요. >>> ")
#     if not schedule:
#         break
#     file.write(schedule + "\n")
# file.close()
'''
p 233

3. 파일 입력(input)
    1. 텍스트 파일 읽기
        1) read() 메서드
        형식 :
            file.read(size)
'''

# file = open("hello.txt", "rt")
#
# str = file.read(2)
# print(str, end="")
#
# file.close()
'''
파일과 동일한 모습으로 출력하기 위해서 print() 함수의 자동 줄바꿈 방지를 위한 end=""속성 추가.

read() 메서드를 통해 전체를 읽으려면 메모리 공간이 많이 필요합니다. 읽어야 할 파일이 크다면
일부만 읽어들이는 작업을 반복하는 반복문을 통해 파일 전체를 읽도록 구현하는 것이 좋다. 
'''
#
# file = open("hello.txt", "rt")
# end_of_text = False
# while not end_of_text:
#     str = file.read(1)
#     if not str:
#         break
#     print(str, end="")
# file.close()

'''
        2) readline() 메서드
            텍스트 파일을 한 줄씩 읽어서 처리하는 메서드
            만약 파일이 종료되어 더 읽어들일 데이터가 없다면 빈 문자열("")을 읽어들입니다.
            반복문을 이용해서 여러 번 읽어들여야 할 때 파일 전체를 읽을 수 있습니다.
'''

# file = open("hello.txt", "rt")
#
# end_of_text = False
# while not end_of_text:
#     str = file.readline()
#     if not str:
#         break
#     print(str, end="")
# file.close()
# print()

'''
        3) readlines() 메서드
            전체 라인을 모두 읽어 각 라인 단위로 '리스트'에 저장하는 메서드
'''
# file= open("hello.txt", "rt")
# line_list = file.readlines()
# for line in line_list:
#     print(line, end="")
#
# file.close()
'''
나라별 수도를 순차적으로 반복시켜 nation 리스트에 사전에 미리 저장해두었습니다.

nation 리스트의 내용을 이해하여 다음과 같은 nation.txt 파일을 생성하세요.

실행 예

생성된 nation.txt 파일의 내용은 다음과 같습니다.

그리스 - 아테네
독일 - 베를린
러시아 - 모스크바
미국 - 워싱턴
'''
nation = ["그리스", "아테네", "독일", "베를린", "러시아", "모스크바", "미국", "워싱턴"]

# 막 쓴 버전
file = open("nation.txt", "wt")
file.write(nation[0] + " - " + nation[1] + "\n")
file.write(nation[2] + " - " + nation[3] + "\n")
file.write(nation[4] + " - " + nation[5] + "\n")
file.write(nation[6] + " - " + nation[7])
file.close()

# 반복문 버전

with open("nation2.txt", "wt") as file:
    # 리스트를 두 항목씩 반복하면서 파일에 작성합니다.
    for i in range(0, len(nation), 2):
        file.write(nation[i] + " - " + nation[i+1] + "\n")












'''
학생들이 다양한 동물들과 그들의 영어 이름을 리스트로 작성했습니다. 이를 바탕으로 animals.txt 파일을 생성하세요

'''

animals = ["고양이", "cat", "강아지", "dog", "코끼리", "elephant", "사자", "lion", "원숭이", "monkey"]

with open('animals.txt', 'wt', encoding='cp949') as file:
    for i in range(0, len(animals), 2):
        file.write(animals[i] + ' - ' + animals[i + 1] + '\n')




# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.field_names = ["분류", "종류", "의미", "설명", "파일이 없을 때 동작", "파일이 있을 때 동작"]
# table.add_row(["입력", "r", "read", "읽기", "오류 발생", "읽기"])
# table.add_row(["출력", "w", "write", "쓰기", "새로 생성", "새로 생성"])
# table.add_row(["", "a", "append", "추가", "새로 생성", "추가"])
# table.add_row(["", "x", "exclusive", "배타적 추가", "새로 생성", "오류 발생"])
#
# print(table)
#
# table2 = PrettyTable()
# table2.field_names = ["종류", "의미", "설명"]
# table2.add_row(["t", "text", "텍스트 파일"])
# table2.add_row(["b", "binary", "바이너리 파일(텍스트 파일 외의 모든 파일)"])
#
# print(table2)
#
# table3 = PrettyTable()
# table3.field_names = ["모드", "설명"]
# table3.add_row(["rt", "텍스트 파일 읽기 모드"])
# table3.add_row(["rb", "바이너리 파일 읽기 모드"])
# table3.add_row(["wt", "텍스트 파일 쓰기 모드"])
# table3.add_row(["wb", "바이너리 파일 쓰기 모드"])
# table3.add_row(["at", "텍스트 파일 추가 모드"])
# table3.add_row(["ab", "바이너리 파일 추가 모드"])
# table3.add_row(["xt", "텍스트 파일 배타적 추가 모드"])
# table3.add_row(["xb", "바이너리 파일 배타적 추가 모드"])
#
# print(table3)
