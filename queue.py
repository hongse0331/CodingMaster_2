queue= []

def push(data):
    queue.append(data)

def pop():
    if(len(queue) == 0):
        return -1
    else:
        return queue.pop(0)

def size():
    return len(queue)

def empty():
    if(len(queue) == 0):
        return 1
    else:
        return 0

def front():
    if(len(queue) == 0):
        return -1
    else:
        return queue[0]

def back():
    if(len(queue) == 0):
        return -1
    else:
        return queue[len(queue)-1]


import sys

n = int(sys.stdin.readline())

for _ in range(n):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == 'push':
        push(cmd[1])
    elif cmd[0] == 'pop':
        print(pop())
    elif cmd[0] == 'size':
        print(size())
    elif cmd[0] == 'empty':
        print(empty())
    elif cmd[0] == 'front':
        print(front())
    elif cmd[0] == 'back':
        print(back())