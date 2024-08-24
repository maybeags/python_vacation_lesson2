# Scope - 범위
# 지역변수 - 함수 내부에 정의된 변수
# 전역변수 - 함수 외부에 정의된 변수

# enemies = 1                 # 전역변수인 enemies = 1
#
# def increase_enemies():
#     enemies = 2            # 지역변수인 enemies = 2
#     print(f"함수 내부의 적은 {enemies}명입니다.")
#
#
# increase_enemies()
# print(f"함수 외부의 적은 {enemies}명입니다.")
# print(f"함수 내부의 적은 {enemies}명입니다.")


# 지역 변수가 외부로 전달되지 않는 사례
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()
# print(potion_strength)

# Global scope
player_health = 10
def game():
    def drink_potion():
        global player_health            # 지양되는 코딩 방식
        player_health += 2
        print(player_health)

    drink_potion()

game()



# game_level = 3
# def create_enemy():
#     enemies = ["skeleton", "zombie", "ailen"]
#     if game_level < 5:
#         new_enemy = enemies[0]
#
#     print(new_enemy)
#
# create_enemy() # 해당 부분은 new_enemy가 if 내부에 있어도 불러낼 수 있다.
'''
if, while, for와 같이 콜론과 같이 들여 쓰기가 있는 모든 코드 블록은
지역범위를 만드는 것으로 간주되지 않습니다.  -> 지역변수라는 용어의 정의에 주목해야 합니다.
지역 변수 : 함수 내부에 정의된 변수
'''