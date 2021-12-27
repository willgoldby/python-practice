def print_rug(size):
    N, M = map(int, size.split())
    for i in range(1,N,2): 
        print((i * ".|.").center(M, "-"))
    print("WELCOME".center(M,"-"))
    for i in range(N-2,-1,-2): 
        print((i * ".|.").center(M, "-"))



if __name__ == '__main__':
    some_input = input() 
    print_rug(some_input)
