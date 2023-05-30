def flippingBits(n):
    # Write your code here
    binary = bin(n)[2:]
    missing_bits = 32 - len(binary)
    missing_zeros = missing_bits * "0"
    binary = missing_zeros + binary

    flipped = "0b"
    for i in range(len(binary)):
        bit = binary[i]
        new_bit = "1" if bit == "0" else "0"
        flipped += new_bit

    return int(flipped, 2)

print(flippingBits(2147483647))
