def pal (n):
    if str(n)==str(n)[::-1]:
        return "palindrome"
    else :
        return " not palindrome "

n=int(input("Enter the number :"))
print(pal(n))