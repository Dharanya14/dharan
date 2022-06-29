def string(str1, substr):
    a=str1.split()
    count=0
    for i in range(0,len(a)):
        if(substr==a[i]):
            count=count+1
    return count
strl=input("enter your string:")
substr+input("enter your substring:")
b=string(strl,substr)
printf("how times substring present:()".format(b))
