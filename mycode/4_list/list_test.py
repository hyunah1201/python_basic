'''
    list 타입을 선언하고, list에 엘리먼트 추가, 삭체
'''

num_list = [60,10,30,70,80]
num_list2 = [1,2,3,4,5]

# 리스트의 메모리 저장 방식
print(num_list, num_list2)
num_list2 = num_list
print(num_list, num_list2)
num_list.sort()
print(num_list, num_list2)
num_list2 = [1,2,3,4,5]
num_list.sort()
print(num_list, num_list2)

print(type(num_list), num_list)
print(num_list[0], num_list[0:3], num_list[3:])

for idx, num in enumerate(num_list):
    print(idx, num)

str_list = ['python', 'java', 'kotlin', 'C++', 'Scalar']
print(type(str_list), str_list)
# index로 list의 엘리먼트 값 변경
str_list[1] = 'java script'
print(str_list[1], str_list[2:4])
# 엘리먼트 추가
str_list.append('Cobol')
str_list.insert(1, 'type script')
print(str_list)
# 엘리먼트 삭제
str_list.remove('Cobol')
del str_list[0]
del str_list[:3]
print(str_list)

print(str_list * 2) # 리스트 2번 출력
print('Scalar' in str_list) # str_list에 Scalar라는 값이 들어있냐?

for idx, val in enumerate(str_list):
    print(idx, val)

mix_list = [100, 3.14, True, '파이썬']
for mix in mix_list:
    print(type(mix), mix)


my_list = list('Python') # str -> list
print(type(my_list), my_list)

my_list2 = 'Hello, Python'.split(',') # str -> list
print(my_list2)

# packing 과 unpacking
# packing : 여러개의 문자열을 한 개의 변수에 모으는 것
my_list3 = ['aa', 'bb', 'bb', 'ab']
print(my_list3.index('bb')) # 값으로 인덱스 찾기
print(my_list3.count('bb'))

# unpacking : 엘리먼트 개수와 받으려는 개수가 같아야
my_list4 = ['dd', 'ff']
my_list3.extend(my_list4) # extend() : 리스트에 새로운 리스트 추가
print(my_list3)

str1, str2 = ['cc', 'dd']
str1, str2 = my_list4
print(str1)
print(str2)

# 2차원 배열


