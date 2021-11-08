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
    for i in range (1,n):
        if(GCD(i,z)==1):
            e=i
    
    for a in range (1,1000):
        if(a!=z and (e*a-1)!= z):
         if((e*a-1) % z == 0):
             d=a
             break

  

    #Encryption
    print("\n        \t  *************ENCRYPTION***************")
    print("Letter \t Numeric Representation \t m^e \t\t\t   Cipher Text")
    
    for i in range(len(string)):
        s = ord(string[i].lower())-96               #convert to alphabet numbers
        x.append(s**e % n);                         #Encryption formula
        print(" ",string[i],"\t",s,"\t",s**e,"\t",x[i])
            
   #Decryption
    print("\n      \t *************DECRYPTION***************")
    print("Cipher Text \t\t\t c^d \t\t\t\t m= m^e mod n \t    Plane Text")

    for i in x:
        k= (i**d) % n 
        w = chr(k + 96)                             #Decryption formula
        print(" ",i,"\t",i**d,"\t",(i**d)**e % n,"\t", w)

EncryptionAndDecryption(p,q,string)


