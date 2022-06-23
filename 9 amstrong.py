n=int(input("enter a number"))
temp=n
while n>0:
      r=n%10
      sum=sum+(r*r*r)
      n=n/10

      if temp==sum:
         print ("amstrong number")
else:
    print("not amstrong number")
