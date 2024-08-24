'''
응용 예제

다음 지시사항을 읽고 책 제목과 저자 정보를 저장할 수 있는 Book클래스를 생성하세요.

지시사항

1. 책 제목과 저자 정보를 출력하는 print_info() 메서드를 구현하세요.
2. 다음과 같은 방법으로 book1과 book2 인스턴스를 생성하세요.

#book1, book2 인스턴스의 생성
book1 = Book()
book2 = Book()

실행 예
책 제목 : 파이썬
책 저자 : 민경태
책 제목 : 어린왕자
책 저자 : 생텍쥐페리
'''

class Book:

    def __init__(self):
        #여기서 작성하세요
        self.title = ""
        self.author = ""

    def set_info(self, title, author):
        self.title = title
        self.author = author

    def print_info(self):
        print(f"책 제목 : {self.title}\n책 저자 : {self.author}")


book1 = Book()
book2 = Book()
book3 = Book()

book1.set_info("파이썬", "민경태")
book2.set_info("어린왕자", "생텍쥐페리")

book1.print_info()
book2.print_info()
book3.print_info()

'''
코드 설명

# 1. 클래스 정의

class Book:

    def __init__(self):
        self.title = ""
        self.author = ""
        
# 2. set_info() 메서드 정의 

    def set_info(self, title2, author2):
        self.title = title2
        self.author = author2

# 해당 메서드에서 두 개의 매개 변수(title2, author2)를 받고, 인스턴스 변수 title와 author를 각각 입력 받은 값으로 설정함.

# 3. print_info() 메서드 정의

    def print_info(self):
        print(f"책 제목 : {self.title}")
        print(f"책 저자 : {self.author}")
        
# 해당 메서드에서 인스턴스 변수 title과 author의 값을 출력함.

# 4. 인스턴스(객체) 생성 및 정보 설정

book1 = Book()
book1.set_info("파이썬", "민경태")
book2 = Book()
book2.set_info(author="생텍쥐페리", title="어린왕자")


    
'''


class Book:

    def __init__(self):
        self.title = ""
        self.author = ""

    # 2. set_info() 메서드 정의

    def set_info(self, title2, author2):
        self.title = title2
        self.author = author2

    # 해당 메서드에서 두 개의 매개 변수(title2, author2)를 받고, 인스턴스 변수 title와 author를 각각 입력 받은 값으로 설정함.

    # 3. print_info() 메서드 정의

    def print_info(self):
        print(f"책 제목 : {self.title}")
        print(f"책 저자 : {self.author}")

        # 해당 메서드에서 인스턴스 변수 title과 author의 값을 출력함.

        # 4. 인스턴스(객체) 생성 및 정보 설정


book1 = Book()
book1.set_info("파이썬", "민경태")
book2 = Book()
book2.set_info(author2="생텍쥐페리", title2="어린왕자")

book1.print_info()
book2.print_info()