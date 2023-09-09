"""This module implements the PocketAES enxryption algorithm.
Muhammad Hassan Raza - 20L-1361 - BSE-7A"""

substitution_box = {
    "0000": "1010",
    "0001": "0000",
    "0010": "1001",
    "0011": "1110",
    "0100": "0110",
    "0101": "0011",
    "0110": "1111",
    "0111": "0101",
    "1000": "0001",
    "1001": "1101",
    "1010": "1100",
    "1011": "0111",
    "1100": "1011",
    "1101": "0100",
    "1110": "0010",
    "1111": "1000",
}


def main():
    """This is the main function."""
    sub_nibbles = []
    shifted_row = []
    MixColumn = []

    text_block = input("Enter a text block: ")
    if len(text_block) > 4:
        print("Input is not valid. It should have exactly 4 characters.")
        return

    text_block = text_block.zfill(4)
    # Convert the hexadecimal to binary and remove the '0b' prefix
    binary_value = bin(int(text_block, 16))[2:]
    binary_value = binary_value.zfill(16)
    sub_nibbles = sub_nibbles_func(binary_value)
    print(f"SubNibbles({text_block}) = ", sub_nibbles)


def sub_nibbles_func(binary_value):
    """This function performs the substitution of nibbles."""
    sub_nibbles_data = []
    for i in range(0, 16, 4):
        sub_nibbles_data.append(substitution_box[binary_value[i : i + 4]])

    hexadecimal_values = []
    for binary_value in sub_nibbles_data:
        # Convert the binary to an integer and then to a hexadecimal nibble
        hex_value = hex(int(binary_value, 2))[2:]

        # Append the hexadecimal nibble to the list
        hexadecimal_values.append(hex_value)

    # Join the nibbles together to get the final output
    hexadecimal_values = "".join(hexadecimal_values)
    return hexadecimal_values


if __name__ == "__main__":
    main()
