calls = 0

def count_calls() :
    global calls
    calls+=1

def string_info(name) :
    count_calls()
    info_str = []
    info_str.append([len(name),str(name).upper(),str(name).lower()])
    return info_str[0][0],info_str[0][1],info_str[0][2]

def is_contains(line,list_) :
    count_calls()
    is_changet = False
    line.lower()
    for i in range(len(list_)) :
        if line.lower() == list_[i].lower() :
            is_changet = True
            break

    return is_changet

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)