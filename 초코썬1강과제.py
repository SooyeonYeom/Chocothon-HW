name = input("키미노 나마에와..?")

print(f"{name}쿤...!기다리고 있었다구..!")

year = 2022
birth = int(input(f"{name}쿤의 몇년도에 태어났어..?와타시 궁금해!"))  # Int = 정수변환

result = year - birth + 1

print(f"그럼 2022년 기준으로 {name}쿤은 {result}살이네! 맞지? \n1. 응 맞아 \n2. 아닌데? ")
ans = input(" ")
if ans == "1":
    print(f"역시 그렇군!")

elif ans == "2":
    print(f"개구라까지마{name}쿤! {result}살 맞잖아!")


result2 = year - birth
result3 = year - birth - 1

print("근데 올해 생일은 지났니?\n1. 지났어\n2. 아직 안 지났어")
choice = input("음, 내 생일은..")
if choice == "1":
    print(f"그럼 {name}쿤은 만으로 {result2}살이네? 후후.. 엄밀한 편이 좋잖아..?")

elif choice == "2":
    print(f"그럼 {name}쿤은 아직 만으로 {result3}살이네? 후후.. 엄밀한 편이 좋잖아..?")

else:
    print(f"{name}쿤,물어본대로만 대답해줄래..?")


print(f"와타시 또 궁금한 거 있어, {name}쿤은 몇월에 태어났어?")
month = int(input("나는.."))

if month == 12 or month == 1 or month == 2:
    print(f"오호라..? 그럼 {name}쿤은 겨울나라에서 온 천사구나..?")

elif 3 <= month <= 5:
    print(f"오호라..? 그럼 {name}쿤은 벚꽃나무에 숨어사는 요정이구나..?")

elif 6 <= month <= 8:
    print(f"오호라..? 그럼 {name}쿤은 바다물결에 쓸려온 인어님이구나..?")

elif 9 <= month <= 11:
    print(f"오호라..? 그럼 {name}쿤은 단풍잎을 쓰다듬는 가을여자구나..?")

else:
    print(f"그런 달은 존재하지 않는다고 아기고양이쨩..?")


print(
    f"이제 우리 서로에 대해 많이 안 것 같아.. 나한테 궁금한 점은 없어?\n1. 네 정체가 뭐야? \n2. 네 얼굴을 보여줘 \n3. 가면 안에 있는 얼굴을 공개해주세요!"
)
Q1 = input(" ")
if Q1 == "1" or Q1 == "2" or Q1 == "3":
    print(f"내 이름은 루피! 앞으로 {name}쿤의 코딩을 도와줄 담당 일진이지!")


else:
    print(f"와타시가 안궁금해...?")
