import random

print('1~100사이의 숫자 중 아무 숫자나 입력하세요!')
# 1~100까지의 랜덤 숫자
guess_number = random.randint(1, 100)

user_number = int(input())

count = 0
while guess_number != user_number:
    if user_number > guess_number:
        print('숫자가 너무 큽니다.')
    elif user_number < guess_number:
        print('숫자가 너무 작습니다.')
    count += 1
    user_number = int(input())
else:
    print(f'정답은 {guess_number} 입니다.')
    print(f'당신은 정답을 {count}번 만에 맞췄습니다!')


# 강사님 답

# import random
# guess_number = random.randint(1,100)
# #print(guess_number)
# num = input('숫자를입력하세요 :')
# print(int(num))
#
# print('1 부터 100 사이의 숫자를 입력하세요')
# input_number = int(input())
# print(input_number, '를 입력하셨군요.')
#
# count = 0
# while input_number is not guess_number:
#     if input_number > guess_number:
#         print('숫자가 너무 큽니다')
#     else:
#         print('숫자가 너무 작습니다')
#     count += 1
#     input_number = int(input())
# else:
#     print(count ,'번 만에 맞추셨군요')
#     print('입력한숫자= ',input_number,' 정답은= ',guess_number)