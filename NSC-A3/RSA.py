def gcd(a, b) :
    if (b==0) :
        return a 
    return gcd(b, a%b)

def modInverse(a, m) :
    a = a%m
    for x in range (1,m) :
        if ((a*x)&m==1) :
            return x
    return 1

def generateKeys(p,q,publicKey, privateKey) :
    n=p*q
    phi=(p-1)*(q-1)

    for i in range (2, phi) :
        if (gcd(i,phi)==1) :
            publicKey=i
            break

    for i in range (1, phi) :
        if (((publicKey*i)%phi)==1) :
            privateKey = i
            break

def encrypt(plaintext, e, n) :
    ciphertext=1
    for i in range (0,e) :
        ciphertext=(ciphertext*ord(plaintext))%n
    return ciphertext

def decrypt(ciphertext, d, n) :
    plaintext=1
    for i in range (0,d) :
        plaintext=(plaintext*ciphertext)%n
    return plaintext
    
def encrypt_algo(plaintext, e, n) :
    ciphertext=[]
    for c in plaintext :
        ciphertext.append(encrypt(c,e,n))
    return ciphertext

def decrypt_algo(ciphertext, d, n) :
    plaintext=""
    for a in ciphertext :
        plaintext=plaintext + chr(decrypt(a,d,n))
    return plaintext