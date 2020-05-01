import math

## Problem 1
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

## Problem 2
def mod_inv(a, m): 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1) : 
        return 0
  
    while (a > 1) : 
        q = a // m 
  
        t = m 
        m = a % m 
        a = t 
        t = y 
        y = x - q * y 
        x = t 
  
 
    if (x < 0) : 
        x = x + m0 
  
    return x 
	
## Problem 3
def mod_exp(x, y, N):
    if y == 0:
        return 1
    else:
        z = mod_exp(x, math.floor(y/2), N)
        if (y % 2) == 0:
            return ((pow(z, 2)) % N)
        else:
            return ((pow(z, 2) * x) % N)
	
## Problem 4
def generate_RSA_keys(p, q):
	print('Generating RSA keys...')
	a = (q - 1) * (p - 1) 
	b = p * q
	c = 3
	
	while gcd(c, a) != 1:
		c = c + 2
	
	return [[b, c], mod_inv(c, a)]
	
	
def decrypt(p, q, C, keys):
	public_key = keys[0][0]
	private_key = keys[1]
	
	a = (p - 1) * (q - 1)
	b = mod_inv(private_key, a)
	return mod_exp(C, b, p * q)

def encrypt(private_key, plain_text):
	key = private_key
	cipher = [(ord(char) ** private_key) % key for char in range(len(str(plain_text)))]
	return cipher
	
def test_encryption(p, q, M):
	keys = generate_RSA_keys(p, q)
	# [[84907, 3], 56187]
	public_key = keys[0][0]
	private_key = keys[1]
	
	print('Public key: %i' % public_key)
	print('Private key: %i' % private_key)
	print('Plain text: %i' % M)
	
	cipher = encrypt(public_key, M)
	print('Cipher text: %i' % cipher)
	
	print(decrypt(p, q, cipher, keys))
		

test_encryption(431, 197, 4)