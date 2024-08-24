from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:                        # 프로그램을 반복 실행시키겠다.
    options = menu.get_items()
    choice = input(f"어떤 음료를 선택하시겠습니까? {options} >>> ").lower()
    if choice == "off":
        is_on = False               # 프로그램을 종료시키겠다.
    elif choice == "report":        # coffee_maker와 money_machine의 .report() 메서드를 실행시키는 구간
        coffee_maker.report()       #
        money_machine.report()      # 여기까지가 실행 구역
    else:                           # 음료 제조 과정
        drink = menu.find_drink(choice)
        if drink == None:
            continue                        # 해당 반복문의 맨 처음으로 돌아가고 이 밑의 실행문은 실행시키지 않겠다
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):      # is_resource_sufficient() 메서드를 확인했을 때, drink.ingredients를 반복돌리는 걸 확인했기 때문에 인수로 drink만 집어넣어도 된다 / drink.ingredients를 하면 오류
            # if money_machine.make_payment(drink.cost):      # make_payment() 메서드를 확인(ctrl+클릭)하면, 매개변수로 cost를 받는 것을 확인, 그리고 해당 메서드 실행시 process_coins()를 실행하는 것을 확인하면 drink.cost를 인수로 요구함을 알 수 있다.
            coffee_maker.make_coffee(drink)             # make_coffee() 메서드를 확인했을 때, drink.ingredients를 조회하는 것을 확인할 수 있었으므로 choice를 인수로 사용할 수 없음.

