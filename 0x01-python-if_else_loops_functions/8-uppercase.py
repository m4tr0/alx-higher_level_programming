def uppercase(s):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            print(chr(ord(char) - 32), end='')
        else:
            print(char, end='')
    print()

