
def arm (n):
  s=0
  c=0
  dis=""
  for i in str(n):
    c=c+1
    s= s+(int(i)**len(str(n)))
    if c < len(str(n)):
       dis=dis+i+"^"+str(len(str(n)))+" + "
    else:
      dis=dis+i+"^"+str(len(str(n)))
  if n==s:
       return print(dis+" = "+str(s)+" armstrong")

  else:
    return print("not armstrong")

def auto (n):
    s=n**2
    if str(n)==str(s)[-len(str(n)):]:
        return True 
    else :
        return False 

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

def pal (n):
    if str(n)==str(n)[::-1]:
        return "palindrome"
    else :
        return " not palindrome "
    
def some(n):
   print(n)