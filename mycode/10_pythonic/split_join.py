# split() : string -> list
# join() : list -> string

my_str = 'java python kotlin'
my_list = my_str.split()
print(type(my_list), my_list)

my_str2 = ''.join(my_list)
print(my_str2)

my_str3 = 'java,python,kotlin'
my_list3 = my_str3.split(',')
print(type(my_list3), my_list3)

my_str4 = '/'.join(my_list3)
print(my_str4)

# replace() : 구분자 치환
result = my_str3.replace(',','?')
print(result)