def fact(n):
    return 1 if n == 1 else n * fact(n-1)


# True if the module is run as a standalone script. If the file is imported
# __name__ = name of the module
if (__name__ == '__main__'):
    print(__name__)
    import sys
    if len(sys.argv) > 1:
        print(fact(int(sys.argv[1])))
