'''
1. 파일 입출력 응용 예제

문제 1 : 개인 금융 관리
지시사항

    1. 재무 데이터 준비 하기:
        개인의 월별 수입과 지출 내역을 담은 텍스트 파일을 만드세요.          - wt 모드로 작성
        예를 들어 '2024-07-23, 수입, 300000'과 같은 형식으로 수입과 지출을 기록합니다.

    2. 재무 데이터 저장하기 :
        위에서 준비한 데이터를 "finance_data.txt" 파일에 저장하세요.
        파일에 각 데이터 항목은 한 줄씩 기록되어야 합니다.

    3. 재무 데이터 분석하기:
        저장된 파일을 읽어와 총 수입과 지출을 계산하세요.
        계산된 총 수입과 총 지출을 콘솔에 출력하세요.

2024-07-09, 수입, 300000
2024-07-17, 지출, 50000
2024-07-20, 수입, 250000
2024-07-23, 지출, 20000
'''
import fileinput

# 수입과 지출 초기화
total_income = 0
total_expense = 0

# 파일 생성 및 데이터 작성
with open("finance_data.txt", "wt") as file:
    file.write("2024-07-09, 수입, 300000\n")
    file.write("2024-07-17, 지출, 50000\n")
    file.write("2024-07-20, 수입, 250000\n")
    file.write("2024-07-23, 지출, 20000\n")

# 파일 읽어와서 데이터 분석
# with open("finance_data.txt", "rt") as file:
#     end_of_text = False
#     while not end_of_text:
#         line = file.readline()
#         if not line:
#             break
#         date, money_type, money = line.strip().split(", ")
#         money = int(money)
#         if money_type == "수입":
#             total_income += money
#         elif money_type == "지출":
#             total_expense += money

# with open("finance_data.txt", "r") as file:
#     for line in file:
#         date, money_type, money = line.strip().split(", ")
#         money = int(money)
#         if money_type == "수입":
#             total_income += money
#         elif money_type == "지출":
#             total_expense += money

# with open("finance_data.txt", "r") as file:
#     end_of_list = False
#     while not end_of_list:
#         line = file.readline()
#         if not line:
#             break
#         line_elements = line.strip().split(", ")
#         money = int(line_elements[2])
#         if line_elements[1] == "수입":
#             total_income += int(money)
#         else:
#             total_expense += int(line_elements[2])
#
# print(f"총 수입: {total_income}원")
# print(f"총 지출: {total_expense}원")

'''
문제 2: 영화 관람 기록 관리

지시사항 :
    1. 관람 기록 준비하기
        - 매일 관람한 영화의 제목과 관람 날짜를 포함하는 기록을 movies.txt 파일에 저장하세요.
        예를 들어, '2024-07-23, 영화제목1'과 같은 형식으로 기록합니다.
        
    2. 관람 기록 추가하기 -> 2024-07-25, 파일럿
        추가하여, 전체 기록을 콘솔에 출력하여 제대로 저장됐는지 확인
        
    3. 관람 기록 조회하기
        파일에서 특정 관람 기록만을 출력하는 기능 추가하세요.
        사용자로부터 조회할 날짜를 입력받아 해당 날짜에 관람한 영화 제목을 출력하세요.
'''
file_path = "movies.txt"

# 파일에 초기 관람 기록 작성
with open(file_path, "wt") as file:
    file.write("2024-07-13, 파묘\n")
    file.write("2024-07-24, 데드풀3\n")

# 새로운 관람 기록 추가
with open(file_path, "at") as file:
    file.write("2024-07-25, 파일럿\n")

# 전체 관람 기록 출력
# with open(file_path, "r") as file:
#     print("--------전체 관람 기록----------")
#     for line in file:
#         print(line.strip())             # \n과 print()함수로 인해 두 번 개행되는 것을 막기 위해 strip() 메서드 사용

#특정 날짜의 기록 조회
# movie_date = input("조회할 날짜를 입력하세요. (형식: YYYY-MM-DD) >>> ")
# # # with open(file_path, "rt") as file:
# # #     for line in file:
# # #         date, title = line.strip().split(", ")
# # #         if date == movie_date:
# # #             print(title)
# #
# # with open(file_path, "r") as file:
# #     end_of_list = False
# #     while not end_of_list:
# #         line = file.readline()
# #         if not line:
# #             break
# #         movie_list = line.strip().split(", ")
# #         date2 = movie_list[0]
# #         title2 = movie_list[1]
# #         if date2 == movie_date:
# #             print(title2)

'''
2. CSV 파일 입출력 응용 예제
    문제 1. 학생 성적 통계
    
지시 사항 :
    1. 학생 성적 데이터 준비
        - 학생들의 이름과 성적 정보를 담은 CSV 파일 "student_scores.csv" 파일을 만드세요.
        예를 들어, "홍길동,90,85,88"과 같은 형식으로 성적 정보를 기록합니다.
        
    2. CSV 파일에 성적 저장하기
        - csv.writer를 사용 학생 성적 데이터를 파일에 저장하세요.
        
    3. CSV 파일에서 성적 분석하기
        - 저장된 CSV 파일을 읽어와 각 학생의 평균 점수를 계산하세요.
        - 평균 점수와 함께 학생 이름을 콘솔에 출력하세요.
'''
import csv

file_path = "student_scores.csv"
# 지시사항 1, 2
with open(file_path, "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["이름","국어","영어","수학"])
    csv_writer.writerow(["홍길동",90,85,88])
    csv_writer.writerow(["김철수",78,82,80])
    csv_writer.writerow(["이영희",92,90,89])

# 지시사항 3 CSV 파일을 읽어와 각 학생의 평균 점수를 계산합니다.
# with open(file_path, mode="r") as file:
#     csv_reader = csv.reader(file)
#     field_names = next(csv_reader)
#     for line in csv_reader:
#         student_name = line[0]
#         total_score = int(line[1]) + int(line[2]) + int(line[3])
#         avg_score = total_score / 3
#         print(f"{student_name}의 성적 : {round(avg_score, 2)}")

# with open(file_path, "r") as file:
#     csv_reader = csv.reader(file)
#     field_names = next(csv_reader)
#     for line in csv_reader:
#         student_name = line[0]
#         k_score = int(line[1])
#         e_score = int(line[2])
#         m_score = int(line[3])
#         total_score = 0
#         scores = [ k_score, e_score, m_score ]
#         for score in scores:
#             total_score += score
#         avg_score = total_score / 3
#         print(avg_score)
'''
map() : 주어진 함수를 반복가능객체(iterable)의 각 요소에 적용하고, 그 결과를 새로운 반복가능객체로 반환

형식 :

map(주어진 함수, 반복가능객체) 형식으로 사용, 필요에 따라 여러 개의 반복가능객체를 사용 할 수도 있음.

주의점 : return값이 map 객체로 반환. -> 다시 반복가능객체 형태로 형변환을 시켜줄 필요가 있음.
'''
# with open(file_path, "r") as file:
#     csv_reader = csv.reader(file)
#     field_names = next(csv_reader)
#     for line in csv_reader:
#         name = line[0]
#         # print(line)
#         scores = list(map(int, line[1:len(line):1]))
#         # print(scores)
#         avg_score = sum(scores) / len(scores)
#         # print(f"{name}의 평균 점수 : {avg_score:.2f}")
#         print(f"{name}의 평균 점수 : {round(avg_score, 2)}")


# numbers = [1, 2, 3, 4, 5]
#
#
# def square(number):
#     return number * number
#
# # squared_list.append(numbers[1]*numbers[1])
#
# squared_numbers = map(square, numbers)
#
# print(type(squared_numbers))
# print(squared_numbers)
#
# squared_list = list(squared_numbers)
#
# print(squared_list)
'''
예제 1 : 온도를 섭씨에서 화씨로 변환하기

온도 리스트가 주어질 때, 섭씨에서 화씨로 변환하는 함수를 작성하고, map을 사용하여 변환된 화씨 온도 리스트를 생성하세요.

화씨 = (섭씨 * 9/5) + 32

지시사항
1. 섭씨 온도를 화씨로 변환하는 함수를 정의하세요.
2. map 함수를 사용하여 섭씨 온도 리스트를 각 요소에 변환 함수를 적용하세요.
3. 결과를 리스트로 반환하여 출력하세요.
'''

# # 함수 정의할 것
# def convert_to_fah(celcius):
#     #변환 공식 적용
#     fah = (celcius * 9 / 5) + 32
#     return fah
#
# c_temps = [0, 20, 37, 100]
# #map 사용하여 섭씨 온도를 화씨로 전환
# f_temps = list(map(convert_to_fah, c_temps))        # map(function, iterable) function 뒤에 소괄호 사용하지 않음.
#                                                     # : ',' 뒤의 반복가능객체가 인수 역할을 하기 때문에
# #리스트 형태로 반환하여 print() 사용해서 결과 출력
# print(f_temps)
'''
예제 2 : 문자열의 길이 계산하기

여러 개의 문자열이 담긴 리스트가 주어질 때, 각 문자열의 길이를 계산하여 리스트로 반환하세요.

지시 사항
1. 문자열의 길이를 반환하는 함수를 정의하세요.
2. map 함수를 사용하여, 문자열 리스트의 각 요소에 길이 계산 함수를 적용하세요.
3. 결과를 리스트로 반환하여 출력하세요.
'''
# # 문자열 길이를 반환하는 함수 정의
# def get_length(word):
#     return len(word)
#
# # 문자열 리스트
# strings = ["apple", "banana", "camel", "developer"]
# # map사용하여 문자열의 길이 계산
# lengths = list(map(get_length, strings))
# # 결과를 리스트로 반환하여 출력
# print(lengths)
#
# #한 번에 쓰는 예시
# # print(list(map(get_length, strings)))
#
# print(list(map(len, strings)))          # 함수 정의 하지 않은 예시

'''
파일 읽기 예외 처리

존재하지 않는 파일을 읽으려 할 때 발생하는 예외를 처리하는 프로그램을 작성하시오.
파일이 존재하지 않으면 사용자에게 파일이 존재하지 않음을 알려주고, 파일이 존재하면 파일 내용을 출력하시오.

지시 사항
1. 사용자로부터 파일명을 입력받는다.
2. 입력받은 파일명을 사용하여 파일을 읽는다.
3. 파일이 존재하지 않으면 디폴트 에러 메시지를 출력합니다.
4. 파일이 존재하면 파일 내용을 출력합니다.
5. 예외가 발생하지 않은 경우 "파일을 성공적으로 읽었습니다."라는 메시지를 출력한다.
6. 프로그램 종료 메시지를 출력한다.
'''
file_path = input("파일명을 입력하세요 >>> ")

try:
    with open(file_path, "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(e)
except Exception:
    print("예상할 수 없는 예외가 발생했습니다.")
else:
    print(content)
    print("파일을 성공적으로 읽었습니다.")
finally:
    print("프로그램을 종료합니다.")