#!/usr/bin/python3
def validUTF8(data):
    # Number of bytes remaining to complete a character
    num_bytes = 0

    # Masks to identify the significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Extract the 8 least significant bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in this character
            if (byte & mask1) == 0:
                # 1-byte character
                continue
            elif (byte & (mask1 | mask2)) == mask1:
                # Invalid first byte (starts with 10xxxxxx)
                return False
            elif (byte & (mask1 | mask2)) == (mask1 | mask2):
                # 2-byte character
                num_bytes = 1
            elif (byte & (mask1 | mask2 | (1 << 5))) == (
                    mask1 | mask2 | (1 << 5)):
                # 3-byte character
                num_bytes = 2
            elif (byte & (mask1 | mask2 | (1 << 5) | (1 << 4))) == (
                    mask1 | mask2 | (1 << 5) | (1 << 4)):
                # 4-byte character
                num_bytes = 3
            else:
                # Invalid first byte
                return False
        else:
            # Check continuation byte
            if (byte & (mask1 | mask2)) != mask1:
                return False
            num_bytes -= 1

    # If num_bytes is not 0, then we have an incomplete character
    return num_bytes == 0
