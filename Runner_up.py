
n = int(input("how many scores? :"))
score = []

for i in range (n):
    num = int(input(f"Enter a score {i + 1}:"))
    score.append(num)

score.sort()
largest = max(score)
Runner = score[-2]
print("The largest score is:", largest)
print("The Runner up score is:", Runner)


#or

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr))[-2])
 
#or

n = int(input())
arr = map(int, input().split())
s = set(arr)
m = sorted(s)
print(m[-2])
