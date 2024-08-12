def person_lister(f):
    def inner(people):
        s = sorted(people, key=lambda x: int(x[2]))
        return [f(person) for person in s]
    return inner

@person_lister
def name_format(person):
    return (lambda p: ("Mr. " if p[3] == "M" else "Ms. ") + p[0] + " " + p[1])(person)

if __name__ == '__main__':
    n = int(input().strip())
    people = [input().split() for _ in range(n)]
    print(*name_format(people), sep='\n')
