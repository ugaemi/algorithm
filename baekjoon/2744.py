eng_str = input()
answer = ''
for s in eng_str:
    answer += s.upper() if s.islower() else s.lower()
print(answer)
