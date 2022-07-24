# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

def is_palindrome():
    word = input("Enter word: ").lower()
    word_rev = []

    #solution 3
    word_rev = word[::-1]

    # solution 2
    #word_rev = ''.join(word[-index] for index in range(1, len(word) + 1))

    # solution 1
    # for index in range(1, len(word)+1):
    #     word_rev += word[-index]

    return word == "".join(word_rev)


print(is_palindrome())


