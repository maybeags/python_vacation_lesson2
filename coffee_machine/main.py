# 상수는 대문자로 표기한다.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24.
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# latte의 우유 양이 나올 수 있도록 print()를 작성하세요.
# input("음료를 선택하세요 >>> ")를 통해 음료를 입력받아 해당 음료의 water양이 나올 수 있도록
#print()를 작성하세요.

#print(MENU["latte"]["ingredients"]["milk"])
#choice = input("음료를 선택하세요 >>> ")
#drink = MENU[choice]
#print(MENU[choice]["ingredients"]["water"])
#print(drink["ingredients"]["water"])

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_sufficient(order_ingredients):
    """주문을 할 수 있으면 True를 반환, 재료가 충분하지 않다면 False를 반환."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"죄송합니다. {item}이(가) 충분하지 않습니다.")
            return False
    return True

def process_coins():
    """투입된 동전들로부터 총합을 계산한 값을 반환"""
    print("동전을 투입하세요.")
    total = int(input("몇 개의 쿼터를 넣으시겠습니까? >>> $")) * 0.25
    total += int(input("몇 개의 다임을 넣으시겠습니까? >>> $")) * 0.10
    total += int(input("몇 개의 니켈을 넣으시겠습니까? >>> $")) * 0.05
    total += int(input("몇 개의 페니를 넣으시겠습니까? >>> $")) * 0.01
    return total

def is_transaction_successful(inserted_coins, drink_cost):
    """total이 cost보다 많을 경우 True 반환, 돈이 부족하다면 False 반환"""
    change = round(inserted_coins - drink_cost, 2)
    if inserted_coins >= drink_cost:
        global profit
        profit += drink_cost
        print(f"잔돈 {change}달러입니다.")
        return True
    else:
        print("돈이 부족합니다. 환불합니다.")
        return False

def make_coffee(drink_name, order_ingredients):
    """전체 resources에서 해당 음료의 ingredients를 차감하고 음료가 나오는 print()실행"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"여기 주문하신 {drink_name}☕ 입니다. 맛있게 드세요.")

is_on = True
while is_on:
    choice = input("어떤 음료를 선택하시겠습니까? (espresso / latte / cappuccino) >>> ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"물 : {resources['water']}ml")
        print(f"우유 : {resources['milk']}ml")
        print(f"커피 : {resources['coffee']}g")
        print(f"수익 : ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


