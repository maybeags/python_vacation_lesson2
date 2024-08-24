'''
p 250

    JSON 파일 입출력
    JSON - JavaScript Object Notation의 줄임말로 자바스크립트 객체 표기법
    속성 - 값의 쌍으로 이루어져있습니다.
    key - value / 중괄호로 감싸져있다.

    JSON은 데이터를 저장하고 교환하는 데 사용되는 가벼운 데이터 교환 형식.
    인간이 읽고 쓰기 쉽고, 기계가 구문 분석하고 생성하기 쉬운 텍스트 형식을 사용함.
    특히 웹 애플리케이션에서 서버와 클라이언트 간의 데이터 교환을 위해 널리 사용됨.

    JSON의 기본 구조
    Json의 데이터는 두 가지 기본 구조를 사용함 : 객체(object)와 배열(array)
        1. 객체(object)
            - 중괄호 {}로 둘러싸여 있으며, 키-값 쌍의 모음입니다.
            - 키는 문자열로 표시되며, 값은 다양한 데이터 타입(문자열, 숫자, 배열, 객체, boolean, null 등)을
            가질 수 있음

        profile = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }

        2. 배열(Array) - 동일한 데이터 타입만 가능
            - 대괄호 []로 둘러싸여 있으며, 순서가 있는 값의 List

        장점 :
            1. 가벼움 : 데이터 크기를 줄여 네트워크 전송 시 효율적
            2. 가독성 : 사람에게 읽고 쓰기 쉬우며, 구조가 단순
            3. 호환성 : 많은 프로그래밍 언어에서 json을 쉽게 처리할 수 있는 라이브러리를 제공함.
            4. 유연성 : 다양한 데이터 유형을 포함할 수 있으며, 복잡한 데이터 구조를 표현할 수 있음.

        단점 :
            1. 데이터 형식 제한 : 대표적인 예시 Date, 그리고 바이너리 데이터는 기본적으로 포함 불가능
            2. 오류 처리 : json 구문이 잘못됐을 경우, 구문 분석 오류가 발생

아래의 dict_list를 이용하여 name_list와 age_list, 그리고 spec_list를 만드시오.



        JSON(JavaScript Object Notation) - 본래 자바스크립트 언어로부터 파생되어 자바스크립트의 구문을 따르지만, 언어
        독립형 데이터 포맷
        프로그래밍 언어나 플랫폼에 독립적이기 때문에 구문 분석 및 JSON 데이터 생성을 위한 코드는 자바, 파이썬 등 다양한 언어에서 쉽게 이용 가능

        {
            "이름공간(key)": "값(value),
            "값 구분자": "각각의 값들은 ','(콤마)로 구분되어야 합니다.",
            "이스케이프": "키가 값에서 큰따옴표를 쓰고 싶으면-특정 문자를 이스케이프 하려면- \" 처럼 문자 앞에 역슬래시를 붙입니다.",
            "자료형": "표현 가능한 자료형은 String, int, boolean, object, list 6개 입니다.",
            "문자열 값": "대괄호로 감싸서 표현됨 - 자바/파이썬과 같음.",
            "숫자": 123456, // 대괄호 없이 표현됨
            "boolean 값": True,
            "null 값": null,
            "object 값": {
                "값1": 123456789,
                "값2": False,
                "값3": {
                    "객체 내부": "객체 위치 가능",
                    "구분자": "key-value 구분은 ':'(콜론)으로 이루어집니다."
                }
            },
            "List 값": [
                "여기에 String을 넣고 싶다면 다시 ""를 써야합니다.",                     # 0번지
                {                                                                   # 1번지
                    "현재 값의 인덱스": 1,
                    "해당 방식처럼": "리스트 안에 여러 값을 넣는 것도 가능"
                },
                [ "리스트", "내부에", "리스트를", "삽입하는 것도", "가능합니다."]        # 2번지
            ],
            "JSON 예시": "마무리"
        }
'''

dict_list = [
    {
        "name": "james",
        "age": 20,
        "spec": [
            175.5,
            70.5
        ]
    },
    {
        "name": "alice",
        "age": 21,
        "spec": [
            168.5,
            60.5
        ]
    }
]

name_list = []
age_list = []
spec_list = []

for person in dict_list:
    name_list.append(person["name"])
    age_list.append(person["age"])
    spec_list.append(person["spec"])

print(name_list)
print(age_list)
print(spec_list)

# import json
#
# #1. json.dumps() : 파이썬 객체를 json 문자열로 변환
# profile = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }
# json_string = json.dumps(profile)
# print(json_string)
# print(type(json_string))        # str 클래스
#
# #2. json.loads() : json 문자열을 파이썬 객체로 변환
# data = json.loads(json_string)
# print(data)
# print(type(data))               # dict 클래스
#
# #3. json.dump() : 파이썬 객체를 json 문자열로 변환하고 파일에 저장
# with open("data.json", "w") as file:
#     json.dump(data, file)
#
# #4. json.load() : 파일에서 json 데이터를 읽고, 파이썬 객체로 변환
# with open("data.json", "r") as file:
#     data2 = json.load(file)
# print(data2)