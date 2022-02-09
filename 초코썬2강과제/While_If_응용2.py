# Challenge1 / 난이도5 / 3번 문제

# 문제 3) 사용자로부터 선택지를 입력 받아, 컴퓨터와 가위바위보하는 게임을 만들어보세요.
#  동시에, 총 세번 먼저 이기면 최종 승리하는 삼세판 규칙을 구현해보세요.


# Quiz3

## <논리 상상> ##
# 1) 일단 사용자한테 인풋으로 가위바위보 문자입력받기
# 2) 타임 슬립 함수로 시간차 두고 동시공개 시키기
# 3) 가위바위보 [ 비기기 / 이기기 / 지기 ] 경우의 수 구현
# 4) 회당 승리가 적립돼야하고, 3회 적립시 최종승리 -> break (+비겼으면 아무에게도 적립되지 않아야함)
# 5) 최종승패가 갈리기 전까지 continue 돼야함


## <풀이 성공> ##

import random
import time


def Count():
    print("\n1..")
    time.sleep(0.5)
    print("\n2...")
    time.sleep(0.5)
    print("\n3....")
    time.sleep(0.5)


dic = {1: "가위", 2: "바위", 3: "보"}
dic2 = {"가위": 1, "바위": 2, "보": 3}

list = []
list2 = []

W = "\n!YOU WIN!"
L = "\n!YOU LOSE!"
T = "\n!TIE!"


print("\n\n삼세판으로 진행되는 컴퓨터와의 가위바위보 게임입니다.")


while True:

    if list.count(1) == 3:
        print("\n!VICTORY! 컴퓨터와의 가위바위보에서 최종승리하셨습니다!")
        break

    elif list2.count(1) == 3:
        print("\n!DEFEATED! 컴퓨터와의 가위바위보에서 최종패배하셨습니다!")
        break

    else:

        com_result = random.randint(1, 3)

        com = dic[com_result]

        user = input("\n당신이 내고 싶은 선택지를 입력해주세요. [ 가위 / 바위 / 보 ] : ")

        user_result = dic2[user]

        Count()

        print(f"\n>>>  COMPUTER : '{com}'  VS   USER : '{user}'    <<<")

        if com_result == user_result:
            print(T)
            continue
        elif user_result == 1 and com_result == 3:
            print(W)
            list.append(1)
            continue
        elif user_result == 2 and com_result == 1:
            print(W)
            list.append(1)
            continue
        elif user_result == 3 and com_result == 2:
            print(W)
            list.append(1)
            continue
        else:
            print(L)
            list2.append(1)
            continue


# 한줄후기 : 너무 재밌었다...최고..(⁎ᵕᴗᵕ⁎)◞♡✧


# 1) < 가위바위보 > : randint 함수 + dictionary를 활용해 구현

# randint함수로 문자 추출이 안되기 때문에, 정수 [ 1 2 3 ] 중 하나를 랜덤으로 추출하게 설정
# 이후 정수[ 1 2 3 ]을  선택지[ 가위 바위 보 ]에 짝짓기 위해 Key-정수 : Value-선택지를 넣어 dic1을 만둚
# 이후 사용자는 문자로 선택지를 입력하기 때문에, Key와 Value가 뒤바뀐 dic2도 만듦
# < 승패판단 : if절로 구성 >
# 사용요소 : A<컴퓨터 선택 값> randint(1,3) & B<유저 인풋이 불러온 딕셔너리 V값> dic2[user]
# 비기기 :  A = B
# 유저승리 :
# B1 & A2
# B3 & A1
# B2 & A3
# 나머지 경우 : 컴퓨터 승리


# 2) < 삼세판 > : if문 + list의 append 함수와 count 함수로 구현

# append로 각자의 회당 승리를 각자의 비어있는 list에 적립시키기로 함!
# 유저의 회당 승리는 list1에, 컴퓨터의 회당 승리는 list2에 '1'로 적립시킴
# if문으로 [ (1)최종승리 / (2)최종패배 / (3)계속진행 ] 구분하고 (1)과 (2)승패조건에 count 함수 활용!
# 유저의 최종승리 = list1에 '1'이 '3'개 있을것
# 유저의 최종패배 = list2에 '1'이 '3'개 있을것

# 즉, append로 각자의 list에 회당 승리 '1'로 적립
# 리스트의 '1'이 먼저 3개가 된 경우를 count로 확인, 최종승패를 나누게함
