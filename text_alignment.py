t = int(input("Enter width:"))
c = 'H'

# top corn
for i in range(t):
    print((c * i).rjust(t - 1) + c + (c * i).ljust(t - 1))

#top piller
for i in range(t + 1):
    print((c * t).center(t * 2) + (c * t).center(t * 6))

## center bridge
for i in range((t + 1) // 2):
    print((c * t * 5).center(t * 6))

## bottom piller
for i in range(t + 1):
    print((c * t).center(t * 2) + (c * t).center(t * 6))

## botto corn
for i in range(t):
    print(((c * (t - i - 1)).rjust(t) + c + (c * (t - i - 1)).ljust(t)).rjust(t * 6))

