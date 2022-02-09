# Challenge1 / 난이도5 / 2번 문제

# 문제 2) 1부터 50까지의 숫자 중 폭탄 숫자를 10개 정하고,
# 컴퓨터와 사용자가 차례로 숫자 하나씩을 말해 폭탄 숫자를 먼저 말하게 되는 사람이 패배하는 게임을 만들어보세요.


# Quiz2

## <논리 상상> ##
# 1) 1부터 50까지 중 폭탄 숫자 10개 정하기... 랜덤모듈로 할 수 있을 듯
# 2) 컴퓨터랑 사용자가 차례로 숫자 하나씩 반복문 안에 넣어서 돌리면 될 듯


## <풀이 성공> ##


import random


print("\n\n1부터 50 중에서 선정된 폭탄 숫자 10개를 먼저 말하게 되는 쪽이 패배하는 게임입니다.")


list = []
nums = random.randint(1, 50)

for i in range(10):
    while nums in list:
        nums = random.randint(1, 50)
    list.append(nums)

list.sort()

end = f"\n↓↓ 폭탄 숫자 공개 ↓↓ \n\n{list}"

while True:

    com = random.randint(1, 50)

    print(f"\n제가 먼저 정하겠습니다. 저는 '{com}'으로 하겠습니다.")

    user = int(input("\n1부터 50까지 중, 마음에 드는 숫자를 말해주세요. :"))

    C = list.count(com)

    U = list.count(user)

    if C == 1:
        print(f"\n!COMPUTER LOSE! 컴퓨터가 선택한 '{com}'은 폭탄 숫자입니다!")
        print(end)
        break
    elif U == 1:
        print(f"\n!YOU LOSE! 당신이 선택한 '{user}'은 폭탄 숫자입니다!")
        print(end)
        break
    else:
        print(f"\n!TIE! 컴퓨터와 당신 모두 폭탄 숫자를 선택하지 않았습니다. \n\n다시 숫자를 선택해주세요.")
        continue


print()
print()
print()


# 후기1) 1~50 중에 10개 랜덤으로 중복 안되게 뽑아서 리스트에 넣는 부분 챌린징했다
#       랜덤으로 한 개씩 뽑아주는 ranint함수 활용 + for문으로 몇개 뽑을건지 정하고, while문으로 중복 방지함!

# 후기2) 리스트의 count 함수 활용해봤다
#      리스트에 포함된 요소 X의 개수를 셀 수 있는 함수인데,
#      해당 X가 리스트에 있는지(==1) 없는지(none) 조사하는 방식으로도 활용할 수 있었음 !
