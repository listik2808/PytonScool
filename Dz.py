first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третее число: "))
if first == second and first == third and second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
elif first!= second and first != third and second != third:
    print(0)