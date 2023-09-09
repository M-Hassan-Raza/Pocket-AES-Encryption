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
    hex_value = "903b"
    # Convert the hexadecimal to binary and remove the '0b' prefix
    binary_value = bin(int(hex_value, 16))[2:]

    # Ensure the binary representation is 16 bits by padding with leading zeros
    binary_value = binary_value.zfill(16)

    print(binary_value)
    text_block = input("Enter a text block: ")


def encrypt(message, key):
    """Encrypts the message using the key."""


if __name__ == "__main__":
    main()
