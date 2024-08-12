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
       return(dis+" = "+str(s)+" armstrong")

  else:
    return("not armstrong")


a=int(input("Enter the no :"))
print(arm(a))