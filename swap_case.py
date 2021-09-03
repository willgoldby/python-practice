# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase # letters and vice versa.

def swap_case(s):
    new_s = ''
    if (0 < len(s) <= 1000):
        for i in s:
            if type(i) == str and i.islower():
                new_s += i.upper()
            elif type(i) == str and i.isupper():
                new_s += i.lower()
            else:
                new_s += i
    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)