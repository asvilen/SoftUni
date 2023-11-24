def get_primes(integers: list):
    def whole_nums(n):
        x = 2
        while x < n:
            yield x
            x += 1

    for num in integers:
        if all((num % whole_num != 0) for whole_num in whole_nums(num)) and num > 1:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

print(list(get_primes([-2, 0, 0, 1, 1, 0])))