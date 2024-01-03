# Implementation of multiplicative inverse
def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def multiplicative_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        # a and m are not coprime, so there's no multiplicative inverse
        return None
    else:
        # Ensure the result is positive
        return (x % m + m) % m

# Example usage:
a = 7
m = 26
inverse = multiplicative_inverse(a, m)
if inverse is not None:
    print(f"The multiplicative inverse of {a} modulo {m} is {inverse}")
else:
    print(f"{a} and {m} are not coprime, so there's no multiplicative inverse.")