input_str = input()
str_list = input_str.split()
answer = ''


for i in range(int(str_list[1])):
    for j in range(int(str_list[0])):
        answer += '*'
    answer += '\n'
print(answer)
