import math
import random
import pyfiglet
from rich import print
from termcolor import colored, cprint


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_prime_number():
    while True:
        p = random.randint(2**15, 2**16)
        if is_prime(p):
            return p


def generate_keypair():
    p = generate_prime_number()
    q = generate_prime_number()

    n = p * q
    phi = (p - 1) * (q - 1)

    # Find e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randint(2, phi - 1)
    while math.gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Find d such that d*e % phi = 1
    d = pow(e, -1, phi)

    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key


def display_menu():
    print("1. Generate private and public Keys ")
    print("2. Exit")


def main():
    
    public_key = None
    private_key = None
    title = pyfiglet.figlet_format('RSA GenKeys')
    print(f'[magenta]{title}[/magenta]')
    print("=======================_BY pootinx_==========================" )
    while True:
        display_menu()
        
        
        choice = input("Enter your choice: ")
        if choice == "1":
            public_key, private_key = generate_keypair()
            print("Keys generated successfully!")
            print("Public Key (n, e):", public_key)
            print("Private Key (n, d):", private_key)


        elif choice == "2":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
