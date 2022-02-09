# Challenge1 / 난이도3 / 2번 문제

# 문제 2) 월화수목금토일이 담긴 list를 만들고 반복문과 조건문을 사용해 요일별 기분을 출력해보세요. (O)

# Quiz2 요일 중 하나를 인풋값으로 받고, 해당 인풋에 대응되는 기분 출력하기

## <논리 상상> ##
# 1) 일단 월~일요일이 담긴 집합을 만들어야한다
# 2) 각 요일별 기분이 정해져 있고, 해당 요일을 인풋하면 기분이 출력돼야한다
# 3) 리스트말고 딕셔너리를 활용해 쌍으로 묶으면 더 재미질 것 같다 ...! 일단 도전!

## <풀이 성공> ##

# 제목 : 아이유랑 데이트 약속 잡는 남자친구


flag = False


dic = {
    "월요일": "엔 아마 바쁘지 않을까?",
    "화요일": "은 성급해 보이지.. 안 그래?",
    "수요일": "은 뭔가 어정쩡한 느낌이야..",
    "목요일": "은 그냥 내가 왠지 싫어 ㅎㅎ~",
    "금요일": "? 오..좋아!\n\n돌아오는 이번 주 금요일이지? 그때 봐 자기~!",
}


def day(ans):
    v = dic[ans]
    print(f"\n{ans}{v}")


while True:
    if flag:
        ans = input("\n그 날 빼고 골라봐~ : ")

        if ans == "금요일":
            day(ans)
            break
        else:
            day(ans)
            flag = True
            continue

    else:
        ans = input("이번주는 주중에 데이트 하자고? \n\n흠.. 자기는 무슨 요일에 하고 싶은데? : ")

        if ans == "금요일":
            day(ans)
            break
        else:
            day(ans)
            flag = True
            continue


print()
print()
print()


###후기 : level2때 공부한 dictionary 또 한번 응용해보았다!
