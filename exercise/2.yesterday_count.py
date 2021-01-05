'''
    yesterday.txt 파일을 읽어서
    YESTERDAY라는 단어가 몇번 나왔는지 yesterday_lyric.upper().count('YESTERDAY')
    Yesterday라는 단어가 몇번 나왔는지 yesderday_lyric.count('Yesterday')
    yesterday라는 단어가 몇번 나왔는지
'''

# mode - r(read), w(write), a(append), rb(read binary), wb(write binary)
# f = open("yesterday.txt", 'r')
# lyric = f.read()
#
# print('기본 파일')
# print('Yesterday : ', lyric.count('Yesterday'), '번')
# print('YESTERDAY : ', lyric.count('YESTERDAY'), '번')
# print('yesterday : ', lyric.count('yesterday'), '번\n')
#
# lyric_upper = lyric.upper()
# print('upper() 후')
# print('Yesterday : ', lyric_upper.count('Yesterday'), '번')
# print('YESDERDAY : ', lyric_upper.count('YESTERDAY'), '번')
# print('yesterday : ', lyric_upper.count('yesterday'), '번\n')
#
# lyric_lower = lyric.lower()
# print('lower() 후')
# print('Yesterday : ', lyric_lower.count('Yesterday'), '번')
# print('YESTERDAY : ', lyric_lower.count('YESTERDAY'), '번')
# print('yesterday : ', lyric_lower.count('yesterday'), '번')
#
# f.close()

# close()없이 파일 여는 법
# with open('yesterday.txt', 'r') as f:
#     yesterday_lyric = f.read()

# file read를 함수로 선언
def file_read(file_name):
    with open(file_name, 'r') as f:
        lyric = f.read()
        print(lyric)
    return lyric

yesterday_lyric = file_read('yesterday.txt')

print('Number of a word \'Yesterday\' ', yesterday_lyric.upper().count('YESTERDAY'))
print('Number of a word \'Yesterday\' ', yesterday_lyric.count('Yesterday'))
print('Number of a word \'yesterday\' ', yesterday_lyric.lower().count('yesterday'))


