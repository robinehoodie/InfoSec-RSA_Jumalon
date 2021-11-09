p = int(input("Enter a prime number for p: "))
q = int(input("Enter a prime number for q: "))

def checkPrime(a):
    if(a==2):
        return True
    elif((a<2) or ((a%2)==0)):
        return False
    elif(a>2):
        for i in range(2,a):
            if not(a%i):
                return False
    return True
 
while(((checkPrime(p)== False)or(checkPrime(q)== False))):
    print("\nNumbers are not prime . Try Again")
    p = int(input("Enter a prime number for p: "))
    q = int(input("Enter a prime number for q: "))
   
string= input("Input text:")

def GCD(e,z):
    while(z!=0):
        e,z=z,e%z
    return e

def EncryptionAndDecryption(p , q, string):
    n= p * q
    z = (p-1) * (q-1)
    x = []
    y = []
    

    for i in range(len(string)):
      
        if(string[i].isupper() == True):
            y.append(True)
        else:
            y.append(False)

  

    for i in range (1,n):
        if(GCD(i,z)==1):
            e=i
    
    for a in range (1,1000):
        if(a!=z and (e*a-1)!= z):
         if((e*a-1) % z == 0):
             d=a
             break

    print("\nValue of p*q = ",n)
    print("Value of (p-1) * (q-1) =", z)
    print("Value of e=",e)
    print("Value of d=", d)
    print("Public key (",n,",",e,")")
    print("Private key (",n,",",d,")")
   #Encryption
    print("\n *************ENCRYPTION***************\n")
#     print("Letter \t Numeric Representation \t m^e \t\t\t   Cipher Text")
  
    for i in range(len(string)):
        s = ord(string[i].lower())-96               #convert to alphabet numbers
        x.append(s**e % n);                         #Encryption formula
        print(x[i], end=' ') 
#         print(" ",string[i],"\t",s,"\t",s**e,"\t",x[i])
    print("\n")
   #Decryption
    print("\n*************DECRYPTION***************\n")
#     print("Cipher Text \t\t\t c^d \t\t\t\t m= m^e mod n \t    Plane Text")
    count = 0
    for i in x:
        
        k= (i**d) % n 
        w = chr(k + 96)                             #Decryption formula
        if(y[count]==True):
            print(w.upper(), end='')
        else:
            print(w,end='')
        count+=1
    print("\n")
         
#         print(" ",i,"\t",i**d,"\t",(i**d)**e % n,"\t", w)   

EncryptionAndDecryption(p,q,string)
