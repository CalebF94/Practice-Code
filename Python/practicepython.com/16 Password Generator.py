# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a
# mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating
# a new password every time the user asks for a new password. Include your run-time code in a main method.
#
# Extra:
#
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import random


def generate_Password():
    weak_words = ["These", "words", "12345", "password", "birthday", "letmein"]
    password = ""

    while password == "":
        strength = input("How strong do you want your password? \n 1) weak \n 2) medium \n 3) strong \n>").lower()
        if strength == "weak":
            password = random.choices(weak_words, k=1)
        elif strength == "medium":
            password = "".join([chr(random.randint(33, 126)) for value in range(1, random.randint(6, 10))])
        elif strength == "strong":
            password = "".join([chr(random.randint(33, 126)) for value in range(1, random.randint(11, 20))])
        else:
            print("Invalid selection. Enter 'weak', 'medium', or 'strong'")

    return password


print(generate_Password())