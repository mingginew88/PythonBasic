### 제어문 : 코드 진행 방향을 변경하는 명령어 (if 문)
# 제어 명령어 사용 --> <명령어> <참or거짓을 나타내는 식(값)> : (colon)
# if 사용 (만약 ~~가 참이면 tab으로 밀려 있는 코드를 실행 해라.)
# 그 외의 경우에 -> else

nVar = 1
print(str(nVar) + "번 출력문")
nVar += 1
print(str(nVar) + "번 출력문")

if False :
    nVar += 1
    print(str(nVar) + "번 출력문")
    nVar += 1
    print(str(nVar) + "번 출력문")
    
nVar += 1
print(str(nVar) + "번 출력문")
nVar += 1
print(str(nVar) + "번 출력문")


nAge = int(input("Input Your Age > "))
nPay = 0

if nAge >= 20 :
    print("You are adult")
    nPay = 1250
else :
    print("You are student")
    nPay = 850

print("The Fare is ", str(nPay), ".")

if nAge >=80 :
    print("You are Senior.")
    pay = 0
elif nAge >= 20 :
    print("You are Adult.")
    pay = 1250
elif nAge >= 8 :
    print("You are Student.")
    pay = 850
else :
    print("You are Baby.")
    pay = 0

# switch case 문을 변경해야하는 경우
# in : 포함되어 있는지
# range(x, y) : x부터 y-1 까지의 범위

nAge //= 10

if nAge in range(8, 11) :
    print("You are Senior.")
    pay = 0
elif nAge in range(2, 8) :
    print("You are Adult.")
    pay = 1250
elif nAge == 1 :
    print("You are Student.")
    pay = 850
else :
    print("You are Baby.")
    pay = 0