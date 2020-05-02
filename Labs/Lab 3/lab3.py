#################
## kbrleson    ##
## COMP-2700   ##
## Spring 2020 ##
#################


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
	result = 1
	b = x
	c = y
	
	while c > 0:
		if (c % 2 == 1):
			result = result * b % N
		
		b = b * b % N
		c = c // 2
	
	return result
		
	
## Problem 4
def generate_RSA_keys(p, q):
	a = (q - 1) * (p - 1) 
	b = p * q
	c = 3
	
	while gcd(a, c) != 1:
		c += 2
	
	return [[b, c], mod_inv(c, a)]
	
## Decrypt encrypted_text given the public_key and private_key
def decrypt(public_key, private_key, encrypted_text):
	N, e = public_key
	return mod_exp(encrypted_text, private_key, N)

## Encrypt plain_text given the public_key
def encrypt(public_key, plain_text):
	N, e = public_key
	return mod_exp(plain_text, e, N)
	
## Returns True for a prime number, False for anything else
def check_prime(any_number):
	if any_number > 1:
		for i in range(2, any_number // 2):
			return any_number % i != 0
	else:
		return False
		
def request_prime_number(second_number=False):
	if (second_number == False):
		prime_number = input("Please enter a prime number: ")
	else:
		prime_number = input("Please enter another prime number: ")
		
	try:
		prime_number = int(prime_number)
	except ValueError:
		print('%s is not a prime number. Please try again!' % prime_number)
		return request_prime_number(second_number)
		
		
	if (check_prime(prime_number)):
		return prime_number
	else:
		print('%i is not a prime number. Please try again!' % prime_number)
		return request_prime_number(second_number)
		
def request_plain_text():
	plain_text = input("Please enter a number you would like to encrypt: ")
	try:
		plain_text = int(plain_text)
	except ValueError:
		print('%s is not a number. Please try again!' % plain_text)
		return request_plain_text()
		
	return plain_text
		
	
## Problem 5
if __name__ == '__main__':
	# Get prime numbers from the user
	first_prime = request_prime_number(False)
	second_prime = request_prime_number(True)
	
	print('Now generating RSA private/public keys with primes %i, %i' % (first_prime, second_prime))
	
	keys = generate_RSA_keys(first_prime, second_prime)
	public_key = keys[0]
	private_key = keys[1]
	
	print('Done!')
	print('----------------------------------------------------')
	print('Public key: [%i, %i]' % (public_key[0], public_key[1]))
	print('Private key: %i' % private_key)
	print('----------------------------------------------------')
		
	plain_text = request_plain_text()
	print('\nPlain text before encryption: %i\n' % plain_text)
	
	encrypted_text = encrypt(public_key, plain_text)
	print('Encrypted text: %i\n' % encrypted_text)
	
	decrypted_text = decrypt(public_key, private_key, encrypted_text)
	print('Decrypted text: %i\n' % decrypted_text)
