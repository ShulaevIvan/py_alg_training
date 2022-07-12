# find duplicates in string try  1
input_value  = input()
ans = ''
ans_cnt = 0
for i in range(len(input_value )):
    cnt = 0
    for j in range(len(input_value )):
        if input_value [i] == input_value [j]:
            cnt += 1
    if cnt > ans_cnt:
        ans = input_value [i]
        ans_cnt = cnt
print(ans)
        
# optimize

s = input()

print(max(map(lambda x: (s.count(x), x), s))[1])

