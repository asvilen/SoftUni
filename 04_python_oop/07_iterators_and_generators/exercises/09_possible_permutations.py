import itertools


def possible_permutations(inputs: list):
    # result = [0] * len(inputs)
    # yield inputs
    # i = 1
    # while i < len(inputs):
    #     if result[i] < i:
    #         if i % 2 == 0:
    #             inputs[0], inputs[i] = inputs[i], inputs[0]
    #         else:
    #             inputs[result[i]], inputs[i] = inputs[i], inputs[result[i]]
    #         yield inputs
    #         result[i] += 1
    #         i = 1
    #     else:
    #         result[i] = 0
    #         i += 1

    for perm in itertools.permutations(inputs):
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]
