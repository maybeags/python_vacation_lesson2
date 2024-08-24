from prettytable import PrettyTable
from pokemon_data import pokemon_data

print(pokemon_data[24][1])

# table = PrettyTable()
#
# table.field_names = [ "번호", "이름", "속성" ]
# table.add_row((1, "이상해씨", "풀/독"))
# table.add_row((2, "이상해풀", "풀/독"))
# table.add_row((3, "이상해꽃", "풀/독"))

# print(table)

table = PrettyTable()

table.field_names = [ "번호", "이름", "속성" ]

# 반복문을 실행
for pokemon in pokemon_data:
    table.add_row(pokemon)

print(table)