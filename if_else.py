
n = int(input("Enter a number {i}:"))

if n%2 == 0:
        if n<5:
            print("It is a even number Not -weird")
            
        elif n >= 6 and n <= 20:
            print("It is a even number -Weird")

        elif n > 20:
            print("It is a even number -Not weird")

else:
    print("It is a odd number -weird")
            
