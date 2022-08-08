celcius=input()
l=len(celcius)
c=0
f=0
k=0
if(celcius[l-1]=='C' or celcius[l-1]=='c'):
    n=float(celcius[:l-1])
    c=round(n,2)
    print(str(c)+"C")
    f=(c*1.8)+32
    print(str(round(f,2))+"F")
    k=c+273
    print(str(round(k,2))+"K")
elif(celcius[l-1]=='F' or celcius[l-1]=='f'):
    n=float(celcius[:l-1])
    f=n
    c=(f-32)*(5/9)
    print(str(round(c,2))+"C")
    print(str(round(f,2))+"F")
    k=c+273
    print(str(round(k,2))+"K")
elif(celcius[l-1]=='K' or celcius[l-1]=='k'):
    n=float(celcius[:l-1])
    k=n
    c=k-273
    print(str(round(c,2))+"C")
    f=(c*1.8)+32
    print(str(round(f,2))+"F")
    print(str(round(k,2))+"K")