def checksum(data):
    """Calculate 16-bit checksum for given binary data."""
    if len(data) % 2 != 0:  # If odd, pad with a zero
        data += '0'

    sum_value = 0
    for i in range(0, len(data), 16):  # Process 16-bit chunks
        chunk = int(data[i:i+16], 2)  # Convert chunk to integer
        sum_value += chunk
        sum_value = (sum_value & 0xFFFF) + (sum_value >> 16)  # Handle carry

    checksum_value = ~sum_value & 0xFFFF  # Take 1's complement
    return format(checksum_value, '016b')  # Return 16-bit binary string

def verify_checksum(data, received_checksum):
    """Verify if received checksum is correct."""
    calculated_checksum = checksum(data)
    total_sum = int(calculated_checksum, 2) + int(received_checksum, 2)
    return total_sum & 0xFFFF == 0xFFFF  # Should be all 1s (0xFFFF)

# Example Usage
dataword = "1011011011001011"  # Example binary data (16-bit)
computed_checksum = checksum(dataword)
print("Computed Checksum:", computed_checksum)

# Verification
is_valid = verify_checksum(dataword, computed_checksum)
print("Is the checksum valid?", is_valid)
