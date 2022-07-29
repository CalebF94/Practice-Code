# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of
# happy numbers up to 1000.
#
# (If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes,
# happy numbers are a real thing in mathematics - you can look it up on Wikipedia. The explanation is
# easier with an example, which I will describe below.)

def read_file(file_name):
    out_list = []
    with open(file_name) as f:
        line = f.readline()
        while line:
            out_list.append(int(line.strip()))
            line = f.readline()
    return out_list


primes = read_file("23 Prime Numbers.txt")
happies = read_file("23 Other Numbers.txt")

overlap = [items for items in primes if items in happies]
print(overlap)