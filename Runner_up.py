
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