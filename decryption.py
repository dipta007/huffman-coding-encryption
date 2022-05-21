import decimal

from utility import (
    binary_add,
    binary_multiply,
    binary_sub,
    binary_to_decimal,
    decimal_to_binary,
    reverse_binary,
    two_complement,
)


def decrypt(code, secret_key_a, secret_key_b, rem):
    # x = binary_multiply(code, secret_key_b)
    x = binary_to_decimal(code) * binary_to_decimal(secret_key_b)
    x = decimal_to_binary(x)
    x = binary_add(x, rem)
    x = two_complement(x)
    x = binary_sub(x, secret_key_a)
    x = reverse_binary(x)
    x = binary_sub(x, "1")
    return x


if __name__ == "__main__":
    x = ("1101101", "10010", "1001", "101")
    print(decrypt(x[2], x[0], x[1], x[3]))
