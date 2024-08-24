import random
from hangman_art import logo, stages
from hangman_word_list import word_list

# word_list = ["apple", "banana", "camel"]

#TODO-1 - word_list에서 단어 하나를 임의적으로 선택하고, 해당 단어를 chosen_word라는 변수에 담으세요

chosen_word = random.choice(word_list)
# print(chosen_word)

#TODO-2 - 유저에게 알파벳을 하나 추측해서 입력하라고 요청하고, 이를
# guess라는 변수에 담으세요. 해당 input을 소문자로 변환시키세요.

word_len = len(chosen_word)

#TODO-8 - 남은 목숨 수를 추적하기 위한 변수 "lives"를 만드세요. lives를 6으로 설정하세요.
lives = 6

#TODO-9 - 추측한 글자가 chosen_word에 없으면, "lives"를 1 감소시키세요.
# "lives"가 0이 되면 게임을 멈추고, "졌습니다, 다음 기회에"를 출력해야 합니다.

should_continue = True
end_of_game = False

#TODO-4 - 빈 리스트 display를 만드세요.
#TODO-5 - chosen_word의 각 글자마다, display에 "_"를 추가하세요.
# 예를 들어 chosen_word가 "apple"이라면, display는 ["_", "_", "_", "_", "_"]이 되어야합니다.

display = []
for _ in range(word_len):
    display.append("_")
# print(display)

#TODO-7 - 사용자가 다시 추측할 수 있도록 while 반복문을 사용하세요. 사용자가 chosen_word의
# 모든 글자를 맞추고 "display"에 더이상 빈칸 ("_")이 없을 때만 반복문을 멈추도록 합니다.
# 그 후 사용자가 이겼다고 알려줄겁니다.

print(logo)

while not end_of_game:
# while ''.join(display) != chosen_word:

    guess = input("문자를 추측하세요 >>> ").lower()
    # TODO-3 - 해당 문자가 chosen_word의 문자와 일치하는지를 확인하세요.

    # TODO-6 - chosen_word의 각 위치를 반복하세요. 만약 그 위치의 글자가 "guess"와 일치하면,
    # 그 위치의 display에서 해당 글자를 공개하세요.
    # 예: 사용자가 "p"를 추측했고, chosen_word가 "apple"이라면,
    # display는 ["_", "p", "p", "_", "_"]이 되어야 합니다.

    # 추측한 글자가 맞는지 확인
    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # print(display)
    print(' '.join(display))

    # user가 틀렸는지 확인
    if guess not in chosen_word:
        print("잘못 추측하셨습니다. life를 잃었습니다.")
        lives -= 1
        print(stages[lives])
        # print(lives)
        if lives == 0:
            print("졌습니다. 다음 기회에")
            print(f"정답은 {chosen_word}였습니다.")
            end_of_game = True

    # if ''.join(display) == chosen_word:
    if "_" not in display:
        end_of_game = True
        print("당신이 이겼습니다!")