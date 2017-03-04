'''
BY Carlo Morales
RSA crypto system
'''

import random
import numpy as np


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('+str(a)+' and '+str(m)+' are not coprime')
    else:
        return x % m

mapping = {'a': '99', 'b': '01', 'c': '02', 'd': '03', 'e': '04', 'f': '05',
           'g': '06', 'h': '07', 'i': '08', 'j': '09', 'k': '10', 'l': '11',
           'm': '12', 'n': '13', 'o': '14', 'p': '15', 'q': '16', 'r': '17',
           's': '18', 't': '19', 'u': '20', 'v': '21', 'w': ' 22', 'x': '23',
           'y': '24', 'z': '25', ' ': '26', '.': '27', ',': '28', 'A': '29',
           'B': '30', 'C': '31', 'D': '32', 'E': '33', 'F': '34', 'G': '35',
           'H': '36', 'I': '37', 'J': '38', 'K': '39', 'L': '40', 'M': '41',
           'N': '42', 'O': '43', 'P': '44', 'Q': '45', 'R': '46', 'S': '47',
           'T': '48', 'U': '49', 'V': '50', 'W': '51', 'X': '52', 'Y': '53',
           'Z': '54', ',': '55', '!': '56', '@': '57', '#': '58', '$': '59',
           '%': '60', '^': '61', '&': '62', '*': '63', '(': '64', ')': '65',
           '-': '66', ' ': '00'}


def factor_brute_force(N):
    '''
    This function checks if any number fom numbers from 2 to sqrt(N) is
    a factor of N.We can restrict this to odd numbers to speed up the process.
    '''
    for i in range(2, int(round(N**.5)+1)):
        div = N/float(i)
        if round(div)*i == N:
            print(str(i) + " is a factor of "+str(N))
            return(str(N) + " is not a prime number.)
            break
        else:
            if i == round(N**.5):
                return(str(N)+" is a prime number")


def exp_mod_n(a, exp, N):
    '''
    function to find a^exp mod (N)
    '''
    e = bin(exp)[2:]
    x_1 = 1
    x_2 = a

    for i in list((range(len(e)))):
        if e[i] == '0':
            x_2 = x_1*x_2 % N
            x_1 = x_1**2 % N
        else:
            if e[i] == '1':
                x_1 = x_1*x_2 % N
                x_2 = x_2**2 % N
    return(x_1)


def primality_test(p):
    '''
    If a is not divisible by p, Fermat's little theorem is equivalent to the
    statement that a^p-1-1 is an integer multiple of p, or in symbols a^(p-1)
    equiv 1 mod p
    '''
    mod = exp_mod_n(2, p-1, p) == 1
    if mod is True:
        print(str(p) + " is probably prime ")
    if mod is False:
        print(str(p) + " is not prime! ")


def produce_prime(length=500):
        '''
        length - prime number will have at least 'length' digits.

        If a is not divisible by p, Fermat's little theorem is equivalent to
        the statement that a^p-1-1 is an integer multiple of p, or in symbols
        a^(p-1) equiv 1 mod p
        '''
        a = 1**length
        b = 9**length
        p = random.randint(a, b)
        finish = 0
        while finish == 0:
            p += 1
            mod = exp_mod_n(2, p-1, p)
            if mod == 1:
                finish = 1
                return(p)


def replace_all(text):
    for i, j in mapping.iteritems():
        text = text.replace(i, j)
    return text


# convert string to numeric
def add_padding(string, pad_mod=311):
    L = len(string)
    blocks = L/3+1
    start = 0
    end = 3
    block = list()
    for i in range(blocks):
        temp = string[start:end]
        start = end
        end = end + 3
        out = 0
        for j in range(len(temp)):
            out = out + int(replace_all(temp[j]))*(pad_mod**(2-j))
        if len(temp) != 0:
            block.append(out)
    return(block)


def replace_all_2(text):
    if len(text) == 1:
        text = '0'+text
    for i, j in mapping.iteritems():
        text = text.replace(j, i)
    return text


def remove_padding(block, pad_mod=311):
    strings = []
    for code in block:

        temp_remainder_1 = code/pad_mod**(2)
        temp_mod_1 = code % pad_mod**(2)

        temp_remainder_2 = temp_mod_1 / pad_mod
        temp_mod_2 = code % pad_mod

        temp_remainder_3 = temp_mod_2

        output = [temp_remainder_1, temp_remainder_2, temp_remainder_3]
        out = [replace_all_2(str(x)) for x in output]
        strings = strings + out
    return(''.join(strings))


class RSA():

    def generate_key(self, length_p, length_q, length_e):
        p = produce_prime(length_p)
        q = produce_prime(length_q)
        e = produce_prime(length_e)

        N = p*q
        d = modinv(e, (p-1)*(q-1))
        return({'p': p, 'q': q, 'e': e, 'N': N, 'd': d})

    def encrypt(self, message, e, N):
        padding = add_padding(message, 311)
        secret = []
        for block in padding:
            secret = secret + [exp_mod_n(block, e, N)]
        return(secret)

    def decrypt(self, message, d, N):
        secret = []
        for block in message:
            secret = secret + [exp_mod_n(block, d, N)]
        padding = remove_padding(secret, 311).strip()
        return(padding)
