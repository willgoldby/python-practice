# Given an integer N, and N space-separated integers as input, create a tuple T of those N integers Then compute and print the result of hast(T).
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    def hash_input(n, integer_list):
        t = tuple(integer_list)
        if n == len(t):
            print(hash(t))
    hash_input(n, integer_list)