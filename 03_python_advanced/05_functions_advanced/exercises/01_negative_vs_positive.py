numbers = [int(x) for x in input().split()]
positive_numbers = [x for x in numbers if x > 0]
negative_numbers = [x for x in numbers if x < 0]
positive_sum = sum(positive_numbers)
negative_sum = sum(negative_numbers)
print(negative_sum)
print(positive_sum)
if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")