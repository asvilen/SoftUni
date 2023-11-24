def fibonacci():
    fib_nums = [0, 1]
    for num in fib_nums:
        yield num
        fib_nums.append(fib_nums[-1] + fib_nums[-2])


generator = fibonacci()
for i in range(5):
    print(next(generator))

print("=="*10)

generator = fibonacci()
for i in range(1):
    print(next(generator))