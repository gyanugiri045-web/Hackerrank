def split_and_join(line):
    line = line.split(" ")      
    line = "-".join(line)       
    return line


line = input("Enter a sentence:")
result = split_and_join(line)
print(result)
