# Implementation of Mix column in AES
def mix_columns(state):
    # Define the fixed Galois multiplication matrix
    mix_column_matrix = [
        [0x02, 0x03, 0x01, 0x01],
        [0x01, 0x02, 0x03, 0x01],
        [0x01, 0x01, 0x02, 0x03],
        [0x03, 0x01, 0x01, 0x02]
    ]

    new_state = [[0] * 4 for _ in range(4)]

    for col in range(4):
        for row in range(4):
            result = 0
            for i in range(4):
                result ^= galois_multiplication(mix_column_matrix[row][i], state[i][col])
            new_state[row][col] = result

    return new_state

def galois_multiplication(a, b):
    result = 0
    for _ in range(8):
        if b & 1:
            result ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x11B  # AES irreducible polynomial
        b >>= 1
    return result

# Example usage:
# state is a 4x4 matrix (list of lists) representing the current state
state = [
    [0x32, 0x88, 0x31, 0xE0],
    [0x43, 0x5A, 0x31, 0x37],
    [0xF6, 0x30, 0x98, 0x07],
    [0xA8, 0x8D, 0xA2, 0x34]
]

result = mix_columns(state)
print(result)