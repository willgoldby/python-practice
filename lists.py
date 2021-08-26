# Take list commands as input and modify the list.  

if __name__ == '__main__':
    N = int(input())
    l = []
    input_command = []
    num_commands = 0
    def insert():
        l.insert(int(input_command[1]), int(input_command[2]))
    def append():
        l.append(int(input_command[1]))
    def printing():
        print(l)
    def remove():
        l.remove(int(input_command[1]))
    def sort():
        l.sort()
    def pop():
        l.pop()
    def reverse():
        l.reverse()
    command = {
        'insert': insert, 'append': append, 'print': printing, 'remove': remove,
        'sort': sort, 'pop': pop, 'reverse': reverse
            }
    if num_commands < N:
        for i in range(N):
            #print(f'this is the input: {input()}')
            input_command = input().split(' ')
            #print(f'command:{input_command}')  
            command[input_command[0]]()
        num_commands += 1