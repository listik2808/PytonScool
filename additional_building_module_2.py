import random

def checking_pair(number_one,number_tho) :
    if len(result) == 0 :
        return False
    for i in range(len(result)):
        if result[i] == [number_one, number_tho]:
            return True
    else:
        return  False

number_random = random.randrange(3,20)
result =[]
for i in range(1,number_random) :
    for j in range(1,20) :
        if i == j :
            continue
        if number_random % (i + j)  == 0 :
            is_checking = checking_pair(j,i)
            if is_checking == False :
                result.append([i, j])

print(number_random , "- число из первой вставки")
print(result)
