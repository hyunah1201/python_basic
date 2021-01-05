'''
    문자열 관련 내용들
'''

# escape 문자
greet = 'Hello' * 4 + '\n'
end = '\tGood\'Bye\' !!'
end2 = "\t Good 'Morning' ??"

print(greet + end + end2)

# bool 타입과 str 타입
is_flag = False
my_str = 'False'
print(type(is_flag), type(my_str))

if not is_flag:
    print(my_str)

# 문자열 인덱스(오프셋)
greeting = 'hello world'
print('문자열 길이', len(greeting))

# c언어 스타일
print('파이썬 %s' % greeting)
print('문자열 길이 %i' % len(greeting))

print('문자열 길이 {}, 0번째 인덱스 값은 {}'.format(len(greeting), greeting[0]))
# python 3.6 버전이후 (format함수 안에 여러개 넣어야할 때 보다 가독성을 높이기 위해 사용)
print(f'문자열 길이 {len(greeting)}, 1번째 인덱스 값은 {greeting[1]}')

# 문자열 인덱스 슬라이싱 [start:end:step] step은 default로 1이다. (end값은 n-1 )
print(f'greeting[0:5] = {greeting[0:5]}') #01234
print(f'greeting[6:11] = {greeting[6:11]}') #678910
print(f'greeting[6:] = {greeting[6:]}') #6부터 끝까지
print(f'greeting[:5] = {greeting[:5]}') #처음부터 4까지
print(greeting, greeting[:]) #전체
print(greeting[::2]) #hlowrd

# 음수값의 인덱스 (뒤에서부터 시작)
print(f'greeting[-1:] = {greeting[-1:]}')
print(f'greeting[-2:] = {greeting[-2:]}')
# 역순으로 출력(reverse)
print(f'greeting[::-1] = {greeting[::-1]}')

# 문자열 여러가지 함수들
word = 'Good manufacturing Practice Good'
print(f'대문자로 변환 = {word.upper()}')
print(word.upper())
result = word.upper()
print(word, ' ', result)
print(f'소문자로 변환 = {word.lower()}')
print(word.title())
print(word.find('G'))
print(word.rfind('G'))
print(word.rfind('Good'))
print(word.count('m'))
print(word.count('G'))
word_list = word.split()
print(word_list, type(word_list))
word2 = 'Good/manufacturing/Practice/Good'
print(word2.split('/'))

word3 = ' hello python '
print(len(word3), len(word3.strip()), word3.strip())
print(len(word3.rstrip()), word3.rstrip())

print(word.startswith('G'))
print(word.endswith('G'))

# 낱개 글자 한개씩 쪼개서 출력
for val in word:
    print(val, word.count(val))

print(word_list)
for w in word_list:
    print(w)


hyunah = 'hello, my name is hyunah. Happy new year!'
print(hyunah[-3:])
print(len(hyunah))
print(hyunah[18:-3])
print(hyunah[-6:-3])