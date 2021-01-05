from exercise.fahrenheit import fah_convert

print('변환하고 싶은 섭씨 온도를 입력하세요!')
user_input = input()

result = fah_convert(user_input)

print('섭씨온도 ', user_input)
print('화씨온도 ', round(result, 2))
print('화씨온도 {:.2f} '.format(result))