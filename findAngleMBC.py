# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
if __name__ == '__main__':
    ab = int(input())
    bc = int(input())
    if (0 < ab <= 100) and (0 < bc <= 100):
        ac = math.sqrt((ab)**2 + (bc)**2)
        angleC = round(math.degrees(math.acos(bc/ac)))
        degree_sign = u"\N{DEGREE SIGN}"
        print(f'{angleC}{degree_sign}')