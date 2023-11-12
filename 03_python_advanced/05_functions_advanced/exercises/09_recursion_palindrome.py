def palindrome(*args):
    word = args[0]
    index = args[1]
    if index > len(word) // 2:
        return f"{word} is a palindrome"
    if word[index] != word[-1 - index]:
        return f"{word} is not a palindrome"
    return palindrome(word, index + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
print(palindrome("abba", 0))
print(palindrome("hannah", 0))
print(palindrome("racecar", 0))
print(palindrome("abracadabra", 0))