values_list = [True,"Совсем просто",8]
dictionary = {'a' : 5.123, 'b' : True, 'c' : "text"}
values_list_2 = [25,"C#"]

def print_params(a = 1, b ='строка', c = True) :
    print(a,b,c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(a = [1,2,3],b = 3.5,c = ["Женя","Евгений","Жожа"])
print_params(*values_list)
print_params(**dictionary)
print_params(*values_list_2,42)