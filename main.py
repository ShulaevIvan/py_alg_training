test_arr = [1,2,3,4,5,999, 9,6,8,884]
word_arr = ['aa', 'asdasd','asdggg', 's', 'd']


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

#  find duplicates in string try  2

s = input()
ans = ''
ans_cnt = 0
obj = {}

for now in s:

    if now not in obj:
        obj[now] = 0
    obj[now] += 1

for key in obj:

    if obj[key] < ans_cnt:

        ans_cnt = obj[key]
        ans = key
print(max(obj, key=obj.get))

#  find duplicates in string try  3

s = input()

print(max(map(lambda x: (s.count(x), x), s))[1])


#find num index in arr

def find_index(number, arr):

    ans = -1
    for i in range(len(arr)):
        if ans == -1 and number == arr[i]:
            ans = i
    return ans


print(find_index(999, test_arr))


#find max number in arr

def max_number(arr):

    ans = arr[0]

    for i in range(1, len(arr)):

        if ans < arr[i]:
            ans = arr[i]

    return ans


print(max_number(test_arr))

#find 2 max number in arr

def findmax(arr):
    max1 = max(arr[0], arr[1])
    max2 = min(arr[0], arr[1])

    for i in range(2, len(arr)):

        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2:
            max2 = arr[i]
    
    return (max2, max1)

print(findmax(test_arr))

#find min even

def find_mineven(arr):

    ans = -1
    tumbler = False

    for i in range(len(arr)):

        if arr[i] % 2 == 0 and (not tumbler or arr[i] < ans):
            ans = arr[i]
            tumbler = True
    
    return ans

print(find_mineven(test_arr))

#find min len words in arr

def shortwords(words):

    minlen = len(words[0])

    for word in words:
        if len(word) < minlen:
            minlen = len(word)

    ans = []

    for word in words:

        if len(word)== minlen:
            ans.append(word)

    return ' '.join(ans)

print(shortwords(word_arr))



 