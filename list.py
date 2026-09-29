l = [1,2,3,4,5,7,6]

x = l.insert(2, 9)
print(l)

y = l.remove(1)
print(l)

z = l.append(10)  
print(l)

a = l.sort()
print(l)

b = l.pop(2)    ## pop the number according to the position
print(l)

c = l.reverse()
print(l)



## OR

if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        cmd, *args = input().split()
        if cmd == "insert":
            arr.insert(int(args[0]), int(args[1]))
        elif cmd == "print":
            print(arr)
        elif cmd == "remove":
            arr.remove(int(args[0]))
        elif cmd == "append":
            arr.append(int(args[0]))
        elif cmd == "sort":
            arr.sort()
        elif cmd == "pop":
            arr.pop()
        elif cmd == "reverse":
            arr.reverse()