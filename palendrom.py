name = input("Enter a word:")
str = name[::-1]
if name == str:
    print("It is a palandrom.")

else:
    print("It is not a palandrom")





n = int(input())
nums = input().split()
print(all(int(x) > 0 for x in nums) and any(x == x[::-1] for x in nums))