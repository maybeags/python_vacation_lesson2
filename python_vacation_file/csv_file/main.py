import fileinput
#
# with open("studentList.csv", "wt")  as file:
#     file.write("학번, 이름, 주소, 연락처\n")
#     file.write("10101, 김승별, 서울시 영등포구, 010-1111-1111\n")
#     file.write("10102, 박나라, 서울시 여의도구, 010-2222-2222\n")
#     file.write("10103, 최태욱, 서울시 강남구, 010-3333-3333\n")
#     file.write("10104, 민기홍, 인천시 계양구구, 010-4444-4444\n")
#     file.write("10105, 이명숙, 경기도 과천시, 010-5555-5555\n")
#
# '''
# p 245
#
# 2. CSV 파일 입출력
#     1. CSV 파일 : Comma seperated Values의 약자로, 쉼표로 분리한 값들, 이라는 의미.
#             데이터베이스나 스프레드 시트 데이터를 저장하기 위해서 사용하는 형식.
#             쉼표로 구성된 각 항목들이 '테이블'을 구성하는 각각의 '데이터'가 되는 방식
#
#     2. CSV 파일 읽기 :
#         문자열 처리 메서드를 활용하면 '별도의 외부 모듈이 없어도' 읽는 것이 가능함. -> csv 모듈이 있음 / 문자열 방식으로 읽는 법
#
#         1. 한 줄에 한 데이터가 있기 때문에 readline() 메서드로 한 줄씩 읽는다.
#         2. 쉼표(,)로 분리하기 위해서 split() 메서드를 이용한다. -> String에 딸려있는 메서드 split()
# '''
#
# student_list = []
# with open("studentList.csv", "rt") as file:
#     file.readline()                         # prettyTable의 field_names에 해당함. 학번, 이름, 주소, 연락처
#     end_of_text = False
#     while not end_of_text:
#         line = file.readline()              # 각 프로필들을 한 줄씩 읽어오고
#         if not line:                        # line에 아무 값도 없으면
#             break                           # 종료
#         student = line.split(",")           # 읽어온 라인에서 split() 메서드 사용, ","를 기준으로 요소 분리
#         student_list.append(student)        # 각 요소들을 student_list에 append()함.
# print(student_list)                         # 리스트 내의 리스트 방식으로 콘솔에 출력 -> 첫번째 line은 list에 포함돼있지 않음
#
# '''
# 지시 사항
# studentList.csv 파일에 다음과 같은 프로필을 추가하고, 리스트에 추가된 프로필들을 append() 한 뒤 콘솔에 출력하시오.
#
# 10106, 황종원, 부산시 연제구, 010-6666-6666
# 10107, 하헌석, 부산시 수영구, 010-7777-7777
# 10108, 이정연, 부산시 부산진구, 010-8888-8888
# 10109, 이정민, 부산시 사상구, 010-9999-9999
# '''
#
# with open("studentList.csv", "at") as file:
#     file.write("10106, 황종원, 부산시 연제구, 010-6666-6666\n")
#     file.write("10107, 하헌석, 부산시 수영구, 010-7777-77776\n")
#     file.write("10108, 이정연, 부산시 부산진구, 010-8888-8888\n")
#     file.write("10109, 이정민, 부산시 사상구, 010-9999-9999\n")
#
#
# student_list = []                       # 추가한 부분이 올바른 인덱스에 들어갈 수 있도록 list를 초기화
# with open("studentList.csv", "rt") as file:
#     file.readline()
#     end_of_text = False
#     while not end_of_text:
#         line = file.readline()
#         if not line:
#             break
#         student = line.split(",")
#         student_list.append(student)
# print(student_list)
#
# for student in student_list:            # 리스트 내의 리스트가 아니라 student_list 내의 element를 뽑아오기 위한
#     print(student)                      # 반복문

#
# with open("userList.csv", "wt") as file:
#     file.write('"회원명", 수강과목, 등록일\n')
#     file.write('"강나라", 필라테스, 25일\n')
#     file.write('"나유라", 수영, 25일\n')
#     file.write('"이상기", 헬스, 15일\n')

'''
   간혹 큰따옴표("")를 이용해서 텍스트를 묶는 경우는 큰 따옴표 제거를 해야지 콘솔에서 불러올 수 있음 
'''
#
# user_list = []
# with open("userList.csv", "rt") as file:
#     file.readline()
#     end_of_list = False
#     while not end_of_list:
#         line = file.readline()
#         if not line:
#             break
#         user = line.split(",")
#         user[0] = user[0].strip('"')        # user_list 내의 user가 list 형태이기 때문에, 0번지의 큰따옴표("")를 제거 후 대입
#         user_list.append(user)
# print(user_list)
'''
    문자열 메서드를 사용하여 충분히 이상의 상황들을 잘 처리해낼 수 있지만, 코드 구조가 복잡하고, 정형화되어 반복됨.
    이 경우 자동으로 CSV 파일을 분석하고 처리하는 모듈인 csv 모듈을 사용할 수 있음.
    
    3. csv 모듈로 CSV 파일 생성하기
    
        다음은 주차장에 입고된 차량들을 관리하기 위한 carControll.csv 파일을 생성하는 코드입니다.
'''

import csv

# with open("carControll.csv", "w") as file:
#     csv_maker = csv.writer(file, delimiter=",")
#     csv_maker.writerow(([1, "08러1234", "2024-07-01,14:00"]))
#     csv_maker.writerow(([2, "25다1234", "2024-07-01,14:10"]))
#     csv_maker.writerow(([3, "28하1234", "2024-07-01,14:20"]))
# print("carControll.csv 파일이 생성되었습니다.")

'''
이상의 코드로 작성할 경우 데이터에 불필요한 라인이 하나씩 더 추가되어 있는데,
이를 막기 위해서 새로운 라인을 추가하지 못하도록 newline 옵션을 사용 가능함.
'''

# with open("carControll.csv", "wt", newline="") as file:
#     csv_maker = csv.writer(file, delimiter=",")
#     csv_maker.writerow(([1, "08러1234", "2024-07-01,14:00"]))
#     csv_maker.writerow(([2, "25다1234", "2024-07-01,14:10"]))
#     csv_maker.writerow(([3, "28하1234", "2024-07-01,14:20"]))
# print("carControll.csv 파일이 생성되었습니다.")

'''
이상과 같은 코드가 만들어지는데, 여기서도 문제가 발생할 수 있는 부분이
날짜 다음 쉼표 (,)가 있어 데이터가 3개 row가 아니라 4개 row로 인식되어,
prettyTable 기준으로 fieldnames를 지정하게 되면 오류가 생길 수 있음.
이를 위해 quotechar 옵션 사용 가능
quotechar 옵션은 delimiter 옵션으로 분리되면 안되는 데이터를 묶어주는 문자를 지정할 때 사용 가능함.
이를 ""로 지정하고 최종 반영한 코드는                          -> 큰 따옴표 "" 사이의 쉼표(,)는 데이터 분할하지 않겠다는 의미
'''

# with open("carControll.csv", "wt", newline="") as file:
#     csv_maker = csv.writer(file, delimiter=",", quotechar='"')
#     csv_maker.writerow(([1, "08러1234", "2024-07-01,14:00"]))
#     csv_maker.writerow(([2, "25다1234", "2024-07-01,14:10"]))
#     csv_maker.writerow(([3, "28하1234", "2024-07-01,14:20"]))
# print("carControll.csv 파일이 생성되었습니다.")

'''
    4. csv 모듈로 CSV 파일 읽기
        CSV 파일을 읽기 위해서는 r 모드로 파일을 열고 생성된 파일 객체를 csv.reader() 메서드로 전달하면
        csv.reader() 메서드는 CSV 파일의 내용을 읽고 그 내용을 저장한 객체 (iterator)를 반환합니다.
'''
#
# with open("carControll.csv", "rt", newline="") as file:
#     csv_reader = csv.reader(file, delimiter=",", quotechar='"')
#     for line in csv_reader:         #csv_reader가 반복 가능 객체
#         print(line)
# print(csv_reader)                   # <_csv.reader object at 0x000001C12C5D9EA0> -> 객체이기 때문에 주소값 출력
#

'''
다음 지시사항에 따라 부산광역시 부산진구에 설치된 CCTV의 개수를 구하는 프로그램을 구현하세요.

지시 사항
1. 공공데이터 포털에서 파일을 다운합니다. - 강사 안내
2. 파일 내용은 다음과 같이 구성돼 있습니다.
3. 모든 라인에 존재하는 카메라 대수를 합한 결과를 출력합니다.

실행 예

부산광역시 부산진구에 설치된 CCTV는 총 1000대 입니다.
'''

file_path = "busanJinCCTV.csv"
total_cameras = 0

with open(file_path, "r") as file:
    csv_reader = csv.reader(file)
    # 첫번째 행은 filed_names(prettyTable 기준)에 해당하므로 건너뛰기
    field_names = next(csv_reader)
    for line in csv_reader:         #csv_reader가 반복 가능 객체
        total_cameras += int(line[4])    # '카메라대수' 열의 인덱스를 찾고 total_cameras에 누적적으로 더해주기

print(f"부산광역시 부산진구에 설치된 CCTV는 총 {total_cameras}대 입니다.")





