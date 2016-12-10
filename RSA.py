'''
BY Carlo Morales
RSA crypto system
'''

import random
import numpy as np

a = 10**100
b = 12**100
random.randint(a,b)

p=13
q=97

N=p*q

def factor_brute_force(N):
    '''
    This function checks if any number fom numbers from 2 to sqrt(N) is a factor of N.
    We can restrict this to odd numbers to speed up the process.
    '''
    for i in range(2,int(round(N**.5)+1)):
        div = N/float(i)
        if round(div)*i==N:
            print(str(i)+" is a factor of "+str(N))
            return(str(N)+" is not a prime number. Has factors "+str(int(i)) +" and "+str(int(div)))
            break
        else: 
            if i==round(N**.5):
                return(str(N)+" is a prime number")


p=97

def exp_mod_n(a,exp,N):
    '''
    function to find a^exp mod (N) 
    '''
    e=bin(exp)[2:]
    x_1=1
    x_2=a
    
    for i in list((range(len(e)))):
        if e[i] == '0':
            x_2 = x_1*x_2 % N
            x_1 = x_1**2 % N
        else:
            if e[i] =='1':
                x_1 = x_1*x_2 % N
                x_2 = x_2**2 % N
    return(x_1)
  
def primality_test(p):
    '''
    If a is not divisible by p, Fermat's little theorem is equivalent to the statement that 
    a^p − 1 − 1 is an integer multiple of p, or in symbols
    a^(p-1) equiv 1 mod p
    '''
    mod = exp_mod_n(2,p-1,p) ==1
    if mod == True:
        print(str(p) + " is probably prime ")
    if mod == False:
        print(str(p) + " is not prime! ")
        
for i in range(10000):        
    primality_test(17632847961239864302863218464129846213872186792306418+i )        
        
def produce_prime(len=100):
    '''
    If a is not divisible by p, Fermat's little theorem is equivalent to the statement that 
    a^p − 1 − 1 is an integer multiple of p, or in symbols
    a^(p-1) equiv 1 mod p
    '''
    a = 10**50
    b = 12**50
    p = random.randint(a,b)
    mod = exp_mod_n(2,p-1,p)
    mod = (2**(p-1) % p == 1)
    if mod == True:
        print(str(p) + " is probably prime ")
    if mod == False:
        print(str(p) + " is not prime! ")    


p= 176328479612398464129846213872186792316233

q = 17632847961239864302863218464129846213872186792315991

for i in range(10000):        
    primality_test(176328+i )        
         
e = 186317 

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist .'+str(a)+' and '+str(m)+' are not coprime')
    else:
        return x % m


d = modinv(e,(p-1)*(q-1))
N = p*q
#RSA code exmaple

def padding(string):
    L = len(string)
    blocks = L/3+1
    start = 0
    end =3
    for i in range(blocks):
        print(string[start:end])
        start = end
        end = end +3

string = "This was a fun project."
len(text)

message = 4129306918

encrypt = exp_mod_n(message,e,N)

decrypt= exp_mod_n(encrypt,d,N)
