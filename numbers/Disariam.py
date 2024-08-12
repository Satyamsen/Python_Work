def disa(n):
  
  s=0
  c=0
  
  for i in str(n):
    c=c+1
    s+=int(i)**c
  if s==n:
    return "Disarium"
  else :
    return "Not Disarium"

a=int(input("Enter the no :"))
print(disa(a))