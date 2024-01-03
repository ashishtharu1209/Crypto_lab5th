# Primitive root
def is_primitive_root(g, p):
    if pow(g, p - 1, p) != 1:
        return False
    for i in range(2, p - 1):
        if pow(g, i, p) == 1:
            return False
    return True

def find_primitive_root(p):
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g
    return None

# Example usage:
prime_number = 11
primitive_root = find_primitive_root(prime_number)
if primitive_root is not None:
    print(f"A primitive root of {prime_number} is {primitive_root}")
else:
    print(f"No primitive root found for {prime_number}")