# string = "abracadabra"

# l = list(string)     ## convert string into list
# l[6] = 'm'           ## change the value from string 
# print(l)



def mutate_string(string, position, character):
    c = list(s)
    c[6] = 'c'
    return 

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)