# def my_function():
#   for i in range(1, 21):
#       if i == 20:
#           print("해냈습니다.")
#
#
# my_function()

# import random
# dice_imgs = ["1", "2", "3", "4", "5", "6"]
# dice_num = random.randint(1, 6)
# print(dice_num)
# print(dice_imgs[dice_num-1])
# year = int(input("몇년도에 태어나셨나요? >>> "))
# if year > 1980 and year < 1994:
#     print("당신은 밀레니엄 세대입니다.")
# elif year >= 1994:
#     print("당신은 genZ입니다.")

# age = input("당신의 나이를 입력하세요 >>> ")
# if int(age) > 21:
#    print(f"당신은 {age}살이기 때문에 운전할 수 있습니다.")
#pages = 0
#word_per_page = 0
#pages = int(input("페이지 수 : "))
#word_per_page = int(input("페이지 당 단어수 : "))
#total_words = pages * word_per_page
#print(total_words)

# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
# print(b_list)

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 4, 5, 6])

# mutate([1, 2, 3, 4, 5, 6])
#[2, 4, 6, 8, 10, 12]