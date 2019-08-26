'''RSA crypto system.'''
import random
import numpy as np
import math

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


def egcd(a: int, b: int) -> int:
    """Extended Euclidean Algorithm used to find the gcd of (a, b)

    Arguments:
        a: (int) first integer to use in Extended Euclidean Algorithm
        b: (int) second integer to use in Extended Euclidean Algorithm

    Returns:
        (int) the greatest common denominator of integers a and b
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a: int, m: int) -> int:
    """A modular inverse of an integer a (modulo m) is the integer  a^(-1) such that
        aa^(-1) = 1 (mod m).

        Args:
        a: int which we wish to find modular inverse of
        m: int modulus

        Returns:
            int modular inverse of an integer a (modulo m)
        """

    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception(str(a) + ' and ' + str(m) + ' are not coprime')
    else:
        return x % m


def exp_mod_n(a: int, exp: int, N: int) -> int:
    '''Function to find a^exp mod (N).

    Arguments:
        a: (int) base
        exp: (int) exponent
        N: (int) modulus

    Returns
        (int) solution to a^exp mod (N)
    '''
    e = bin(exp)[2:]
    x_1 = 1
    x_2 = a

    for i in list((range(len(e)))):
        if e[i] == '0':
            x_2 = x_1 * x_2 % N
            x_1 = x_1 ** 2 % N
        #else:
        elif e[i] == '1':
            x_1 = x_1 * x_2 % N
            x_2 = x_2 ** 2 % N
    return x_1


def primality_test(p: int) -> bool:
    ''' If a is not divisible by p, Fermat's little theorem is equivalent to the
    statement that a^p-1-1 is an integer multiple of p, or in symbols a^(p-1)
    equiv 1 mod p.

    Arguments:
        p: (int) which is tested to be a prime number

    Returns:
        (bool) that indicates if the the number p is prime or not
    '''
    mod = exp_mod_n(2, p-1, p) == 1
    if mod is True:
        print(str(p) + " is probably prime ")
        return True
    if mod is False:
        print(str(p) + " is not prime! ")
        return False


def produce_prime(length: int=500) -> int:
    '''length - prime number will have at least 'length' digits.
    If a is not divisible by p, Fermat's little theorem is equivalent to
    the statement that a^p-1-1 is an integer multiple of p, or in symbols
    a^(p-1) equiv 1 mod p.

    Arguments:
        length: (int) minimum length of the prime we wish to find

    Returns:
        (int) a very large prime number based on Fermat's little theorem
    '''
    a = 10**length
    b = 15**length
    p = random.randint(a, b)
    finish = 0
    while finish == 0:
        p += 1
        mod = exp_mod_n(2, p-1, p)
        if mod == 1:
            finish = 1
            return(p)


def replace_all(text: str) -> str:
    """Replace text in a string using a predefined dictionary.

    Arguments:
        text: (str) a sting which we perform text replacement

    Returns:
        (str) a string with possible text replacements

    """
    for i, j in mapping.items():
        text = text.replace(i, j)
    return text


# convert string to numeric
def add_padding(string: str, pad_int: int=311) -> list:
    """Add padding to rsa encryption. Take string blocks and encrypt each on individually.

    Arguments:
        string: (str) string of text being padded
        pad_int: (int) exponent to use in padding scheme

    Returns:
        (list) if encoded integers
    """
    L = len(string)
    blocks = math.floor(L/3) + 1
    start = 0
    end = 3
    block = list()
    for i in range(blocks):
        temp = string[start:end]
        start = end
        end = end + 3
        out = 0

        for j in range(len(temp)):
            out = int(replace_all(temp[j]))*(pad_int**(3-j))
            if len(str(out)) != 0:
                block.append(out)
    return(block)


def replace_all_2(text: str) -> str:
    """Replace text in a string using a predefined dictionary.

    Arguments:
        text: (str) a sting which we perform text replacement

    Returns:
        (str) a string with possible text replacements
    """
    if len(text) == 1:
        text = '0' + text
    for i, j in mapping.items():
        text = text.replace(j, i)
    return text


def remove_padding(block: int, pad_int: int=311) -> str:
    """Add padding to rsa encryption. Take string blocks and encrypt each on individually.

     Arguments:
         block: (int) which is the decoded message that is still padded

     Returns:
         (str) which has the padding scheme reversed and also replaced integers with text
     """
    strings = []
    for k in range(len(block)):

        code = block[k]

        if k % 3 == 0:
            unpadded = code / pad_int**3

        elif k % 3 == 1:
            unpadded = code / pad_int**2

        else:
            unpadded = code / pad_int

        out = replace_all_2(str(int(unpadded)))
        strings.append(out)

    return(''.join(strings))


class RSA():

    def __init__(self, len_p=None, len_q=None, len_e=None, p=None, q=None, e=None, N=None, d=None):
        self.p = p
        self.q = q
        self.e = e
        self.N = N
        self.d = d
        self.len_p = len_p
        self.len_e = len_e
        self.len_q = len_q

    def generate_key(self) -> dict:
        """Create an encryption key.

        Arguments:
            None

        Returns:
            (dict) with p, q, e, N and d which are used to encode and decode messages.
        """
        self.p = produce_prime(int(self.len_p))
        self.q = produce_prime(int(self.len_q))
        self.e = produce_prime(int(self.len_e))

        self.N = self.p * self.q
        self.d = modinv(self.e, (self.p-1) * (self.q-1))
        return({'p': self.p, 'q': self.q, 'e': self.e,'N': self.N, 'd': self.d})

    def encrypt(self, message: str) -> list:
        """Encrypt a string message.

        Arguments:
            message: (str) a sting of text that will be encoded

        Returns:
            (list) a list or integers representing the encoded message.
        """
        padding = add_padding(message, 311)
        secret = []
        for block in padding:
            secret.append(exp_mod_n(block, self.e, self.N))
        return secret

    def decrypt(self, message: list) -> str:
        """Decrypt an encoded message.

        Arguments:
            message: (list) a list of integers representing an encoded message

        Returns:
            (str) which is the decoded string message.
        """
        secret = []
        for block in message:
            secret.append(exp_mod_n(block, self.d, self.N))
        padding = remove_padding(secret, 311)
        return(padding)
