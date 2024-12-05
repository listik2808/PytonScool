numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes = []
not_primes = []
is_primer = True

for i in range(len(numbers)) :
    is_primer = True
    for j in range(numbers[i]):
        if j == 1 or j == 0:
            continue
        elif numbers[i] % j == 0 :
            print(numbers[i],j)
            is_primer = False
            not_primes.append(numbers[i])
            break
    if numbers[i] != 1 and is_primer == True:
        primes.append(numbers[i])

print(primes)
print(not_primes)
