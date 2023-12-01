import math
import random
import pyfiglet
from rich import print
from termcolor import colored, cprint


def generate_keys():
    # Step 1: Generate two distinct prime numbers, p and q
    p = generate_prime()
    q = generate_prime()
    n = p * q

    # Step 2: Calculate Euler's totient function value, phi(n)
    phi = (p - 1) * (q - 1)

    # Step 3: Choose a value for the public exponent, e
    e = find_coprime(phi)

    # Step 4: Calculate the modular multiplicative inverse of e modulo phi(n)
    d = modular_inverse(e, phi)

    return (n, e), (n, d)


def generate_prime():
    # Generate a random prime number between 100 and 1000
    prime = random.randint(100, 1000)
    while not is_prime(prime):
        prime = random.randint(100, 1000)
    return prime


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def find_coprime(phi):
    e = random.randint(2, phi - 1)
    while math.gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    return e


def modular_inverse(a, m):
    _, x, _ = extended_gcd(a, m)
    return x % m


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def encrypt(message, public_key):
    n, e = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message


def decrypt(encrypted_message, private_key):
    n, d = private_key
    decrypted_message = [chr(pow(encrypted_message, d, n))]
    return ''.join(decrypted_message)


def get_input(label):
    return int(input(label))


def get_message(label):
        return input(label)

def display_menu():
    print("1. Generate private and public Keys ")
    print("2. Exit")

def main():   
    title = pyfiglet.figlet_format('RSA GenKeys')
    print(f'[magenta]{title}[/magenta]')
    print("=======================_BY pootinx_========================" )
    print("------------------RSA Encryption and Decryption-------------") 
    while True:
        
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Generate Keys")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = get_input("Enter the public key 'n': ")
            e = get_input("Enter the public key 'e': ")
            message = get_message("Enter the message to encrypt: ")
            encrypted_message = encrypt(message, (n, e))
            print("Encrypted message:", encrypted_message)

        elif choice == 2:
            n = get_input("Enter the private key 'n': ")
            d = get_input("Enter the private key 'd': ")
            encrypted_message = get_input("Enter the message to decrypt: ")
            decrypted_message = decrypt(encrypted_message, (n, d))
            print("Decrypted message:", decrypted_message)

        elif choice == 3:
            public_key, private_key = generate_keys()
            print("Public Key:")
            print("n =", public_key[0])
            print("e =", public_key[1])
            print("Private Key:")
            print("n =", private_key[0])
            print("d =", private_key[1])

        elif choice == 4:
            break

        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()