import random

# 코드를 작성하세요.
ran_num = int(random.randint(1, 20))

for i in range(1, 5):
    screen = int(input(f"기회가 {5-i}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))
    if i == 4:
        print(f"아쉽습니다. 정답은 {ran_num}였습니다.")
        break
    elif ran_num == screen:
            print(f"축하합니다.{i}번 만에 숫자를 맞히셨습니다.")
            break
    elif ran_num != screen:
        if ran_num > screen:
            print("Up")
        else:
            print("Down")