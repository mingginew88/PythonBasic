### 산술 연산자 Arithmetic Operator

var1 = 10
var2 = 25
var3 = 40

money = 43200 # 43200원 -> 43,200 원

print("var1 + var2 = ", var1 + var2)        # add : +
print("var1 - var2 = ", var1 - var2)        # min : -
print("var1 * var2 = ", var1 * var2)        # mul : *
print("var1 / var2 = ", var1 / var2)        # div : /
print("var1 // var2 = ", var1 // var2)      # div : //  (몫)
print("var1 % var2 = ", var1 % var2)        # div : //  (나머지)

# pow : ** (제곱)
print("var1의 제곱은 :",var1**2)

# , 와 + 차이
print("가격 :", money//1000, ",", money%1000, "원")
print("가격 :", str(money//1000), ",", str(money%1000), "원")
print("가격 :" + str(money//1000), ",", str(money%1000)+ "원")

# CPU 연산 작업 (Central Processing Unit)
#   ㄴ컴퓨터 내부의 대부분의 연산은 CPU가 실행
# ALU -> 연산장치 (Arithmetic Logic Unit)