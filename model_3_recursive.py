def get_multiplied_digits(number):
    str_value = str(number)
    first = int(str_value[0])

    if len(str_value) > 1 :
        return first * get_multiplied_digits(int(str_value[1:]))
    else:
        return first if first != 0 else 1
result1 = get_multiplied_digits(402030)
result2 = get_multiplied_digits(40203)
print(result1)
print(result2)
