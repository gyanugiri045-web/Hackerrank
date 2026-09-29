def swap_case():
    text = input("Enter a word:")
    result = text.swapcase()         ## it convert capital letter to small and small to capital 
    print(result)

swap_case()

##or,

def swap_case(s):
    return s.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)