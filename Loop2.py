#반복 제어2 : 횟수를 이용한 반복문
# while -> 잔업 처리 다 할 때 까지 야근
# for   -> 보고서 100page 출력할 때까지 야근
# 어떤 변수의 값이 지정한 범위 안에 있으면 반복
# 범위 밖으로 넘어가면 반복 종료

# i -> 
for i in range(0,10) :
    print(i, 'for 반복 실행')
print('프로그램 종료')

# 실행 순서
# for -> i 변수를 생성 -> range()의 첫번째 값(매개변수)를 대입
# 범위 내의 코드를 실행 -> 제어 끝부분으로 이동 했을 때 다시 i값이 있는 위치로 이동
# 위로 이동할 때 i값을 하나 증가 시킨 후 위쪽으로 이동

var = 0
for i in range(1, 101) :
    if i%2 == 0 : 
        var += i
    else :
        print(str(i) + 'is odd. so skip it.') #break : 실행시 반복 범위 외부로 이동
        # continue : 계속
        continue
        print(str(i) + ' is backside to contnue.')
print("add(1 to 100) --> ", var)

for i in range(2, 10) :
    for j in range(1, 10) :
        print(str(i) + ' * ' + str(j) + ' = ',str(i*j))
