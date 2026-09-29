s = input("Enter a string:")

print(f"The {s} is digit: ", s.isdigit())
print(f"The {s} is lower: ", s.islower())
print(f"The {s} is upper: ", s.isupper())
print(f"The {s} is alpha: ", s.isalpha())
print(f"The {s} is alnum: ", s.isalnum())



## or


if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))