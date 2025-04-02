def xor(a, b):
    result = []
    for i in range(1, len(b)):  # XOR from the second bit
        result.append('0' if a[i] == b[i] else '1')
    return ''.join(result)

def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(tmp, divisor) + dividend[pick]
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(tmp, divisor)
    else:
        tmp = xor('0'*pick, tmp)

    return tmp

def encodeData(data, divisor):
    appended_data = data + '0'*(len(divisor)-1)
    remainder = mod2div(appended_data, divisor)
    return data + remainder

# Example Usage
dataword = "11010011101100"  # Example data
generator = "1011"  # Example divisor (CRC polynomial)
codeword = encodeData(dataword, generator)
print("Encoded Data (Codeword):", codeword)
