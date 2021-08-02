#  Given the participants' score sheet for your University Sports Day, you 
#  are required to find the runner-up score. You are given  scores. Store #  them in a list and find the score of the runner-up.

def runner_up(n, arr):
    arry = []
    for i in arr:
        try:
            arry.append(int(i))
        except:
            continue
    if len(arry) == n:
        arry = set(arry)
        arry = list(arry)
        arry.sort()
        sort_arr = arry
        
        print(sort_arr[-2])
    
if __name__ == '__main__':
    #n = int(input())
    #arr = map(int, input().split())
    n = 4
    arr = [57, 57, -57, 57]
    runner_up(n,arr)
