def check_power(n):
    while n > 1:
        if n % 2 != 0:
            return False
        n //= 2
    return True

n = int(input())
if check_power(n):
    print('Степень двойки')
else:
    print('Не степень двойки')
