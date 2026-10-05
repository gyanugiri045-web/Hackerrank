todos = []

while True:
    task = input("Enter a task or ('q' to quit):")


    if task == "q":
        break

    todos.append(task)


print("Your todo list:")

for todo in todos:
    print("-", todo )
