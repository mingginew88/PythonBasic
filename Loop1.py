# 반복 제어
# <조건식>이 참값인 동안 실행 -> while

# 단일 if 명령어와 생김새는 똑같음

nAge = -1
nPay = 0
sGeneration = ''
while True :
    nAge = -1
    while(nAge < 0) :
        nAge = int(input("Input Age > "))

    if nAge == 0 :
        # 반복 종료 - 보조제어문 break
        break
        
    if nAge >= 80 :
        sGeneration = 'Senior'
        nPay = 0
    elif nAge >= 20 :
        sGeneration = 'Adult'
        nPay = 1250
    elif nAge >= 8 :
        sGeneration = 'Student'
        nPay = 850
    else :
        sGeneration = 'Baby'
        nAge = 0

    print("You are "+ sGeneration +". And your fare is " + str(nPay) +".")
