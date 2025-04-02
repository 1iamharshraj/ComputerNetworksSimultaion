def calculate_parity_bits(data_bits, r):
    parity_positions = [2 ** i for i in range(r)]
    hamming_code = list(data_bits)

    for parity_pos in parity_positions:
        count = 0
        for i in range(1, len(hamming_code) + 1):
            if i & parity_pos:
                count += int(hamming_code[i - 1])
        hamming_code[parity_pos - 1] = str(count % 2)

    return ''.join(hamming_code)


def generate_hamming_code(data_bits):
    m = len(data_bits)
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1

    hamming_code = ['P' if (i & (i + 1)) == 0 else 'D' for i in range(m + r)]

    j = 0
    for i in range(len(hamming_code)):
        if hamming_code[i] == 'D':
            hamming_code[i] = data_bits[j]
            j += 1

    return calculate_parity_bits(hamming_code, r)


# Example Usage
dataword = "1011"
encoded_data = generate_hamming_code(dataword)
print("Hamming Code:", encoded_data)
