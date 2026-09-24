n = int(input("Enter a number:"))

integer_list = map(int, input("Enter a number:").split())
t = tuple(integer_list)
print(hash(t))
