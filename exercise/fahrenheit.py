'''
    섭씨를 입력 받아서 화씨로 변환하는 프로그램
'''

def fah_convert(value):
    fah = ((9 / 5) * float(value)) + 32
    return fah

print('변환하고 싶은 섭씨 온도를 입력하세요!')
user_input = input()

# fah = ((9 / 5) * float(value)) + 32
fah = fah_convert(user_input)

# round() : 반올림 함수
print('섭씨온도', user_input)
print('화씨온도', round(fah, 2))
print('화씨온도 {:.2f} '.format(fah))

