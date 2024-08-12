def wrapper(f):
    def fun(l):
        c = []
        for i in l:
            i = f"+91 {i[-10:-5]} {i[-5:]}"
            c.append(i)
        return f(c)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


