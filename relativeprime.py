# Relative prime
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def are_relatively_prime(x, y):
    return gcd(x, y) == 1

# Example usage:
num1 = 14
num2 = 25

if are_relatively_prime(num1, num2):
    print(f"{num1} and {num2} are relatively prime (coprime).")
else:
    print(f"{num1} and {num2} are not relatively prime.")