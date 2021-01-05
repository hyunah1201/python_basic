'''
    나이 = 현재년도 - 태어난 년도 + 1
    태어난 년도를 입력 받음 input()

    from 모듈명 import datetime모듈 안에 들어있는 datetime클래스
'''

from datetime import datetime as dt

# 현재년도
current_year = dt.today().year
print(dt.today())
print(current_year)

print('태어난 년도를 입력하세요 : ')
input_year = int(input())
age = current_year - input_year + 1

print('태어난 년도 : ', input_year)
print('나이 : ', age)

if 17 <= age < 20:
    print('고등학생')
elif (age >= 20) and (age <= 27):
    print('대학생')
else:
    print('학생이 아닙니다.')