# 반복문 연습
# 아래와 같이 출력하시오.
'''
*
 *
  *
   *
    *
'''

star = '*'
space = ' '

for i in range(0, 5) :
    for j in range(0, 5):
        if i == j :
            print(space*(i) + star)

print('='*50)

output = ''
for i in range(0, 5) :
    for j in range (0, i) :
        output += space
    output += star
    print(output)
    output = ''

print('='*50)


# 아래와 같이 출력하시오.
'''
    *
   *
  *
 *
*
'''

for i in range(1, 6) :
    for j in range(1, 6):
        if i + j == 6 :
            print(space*(5-i) + star)

print('='*50)

for i in range(0, 5) :
    for j in range (0, 4-i) :
        output += space
    output += star
    print(output)
    output = ''

print('='*50)
