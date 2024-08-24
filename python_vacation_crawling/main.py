import requests

'''
pip : 파이썬 패키지 관리자, 파이썬 패키지를 설치하는 데 사용

requests 라이브러리는 파이썬에서 HTTP 요청을 보내기 위해 가장 널리 사용되는 라이브러리 중 하나.
사용하기 쉽고 직관적인 API를 제공하여 HTTP '요청'과 '응답'을 쉽게 처리할 수 있다.
requests 라이브러리를 사용하면 GET, POST, PUT, DELETE 등 다양한 HTTP 메서드를 간편하게 사용할 수 있습니다.

p 315

1. 웹크롤링의 이해
    웹 크롤링(Web crawling)이란 완성된 웹 페이지에서 필요한 정보를 수입하고 선별하여 추출하는 과정
    웹 스크래핑(Web scraping)이라고 하기도 함.
    
    1) HTML의 개념
        Hyper Text Markup Language의 약자로 '웹 페이지를 만드는 문법을 갖춘 언어'라는 의미
        각자의 역할이 정해진 태그들로 구성된 언어로, 페이지를 만드는데 각각의 태그를 붙여가며 사용.
    2) HTML의 구조
    <html>
        head
            meta
            title
        body
            h1
            div
    </html>
    3) URL : Uniform Resource Locator의 약자로 어떤 자원의 위치를 표기하는 방법을 의미함.
    https://www.google.com 과 같은 인터넷 주소를 입력하는데, 이때 입력한 주소가 URL에 해당.
'''
# url = "https://www.naver.com"               # naver 메인 페이지 주소를 url 변수에 저장
# response = requests.get(url)                # requests 모듈의 get() 메서드를 호출하여 결과(response)를 얻어냄
# print(f"응답 코드 : {response.status_code}") # 요청이 정상적으로 처리되었다면 응답 코드를 의미하는 status_code 200을 얻음
# print(response.text)                        # naver.com의 전체 요소를 text 형태로 불러옴
'''
        2. 검색 결과 웹 페이지 정보 가져오기
            네이버에서 "파이썬"을 검색했을 때 나오는 결과 화면을 가져 오는 방법
            
https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=파이썬

입력한 검색어 "파이썬"은 query라는 매개변수로 전달됩니다.
검색어와 관련된 부분은 query매개 변수이기 때문에 나머지를 지워도 검색 결과에는 무방함.
https://search.naver.com/search.naver?query=파이썬
'''
# url = "https://search.naver.com/search.naver"
# param = {
#     "query": "파이썬",
#     "ie": "utf-8"
# }
# response = requests.get(url, params=param)
# print(response.text)

'''
p 321

기본 예제

네이버 웹툰 중 화요 웹툰인 '유부 감자'의 소개 페이지를 가져오는 프로그램입니다.
https://comic.naver.com/webtoon/list?titleId=822556&tab=tue
'''

url = "https://comic.naver.com/webtoon/list"
parameters = {
    "titleId": "822556",
    "tab": "tue"
}
response = requests.get(url, params=parameters)
print(response.text)




