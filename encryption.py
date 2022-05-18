import random
from utility import binary_add, binary_to_decimal, two_complement, reverse_binary, decimal_to_binary

def encrypt(text):
  x = binary_add(text, '1')
  x = reverse_binary(x)

  secret_key_a = x[:random.randint(1, len(x) - 1)]
  secret_key_a = '1101101'
  x = binary_add(x, secret_key_a)
  x = two_complement(x)

  secret_key_b = '0'
  while binary_to_decimal(secret_key_b) == 0:
    secret_key_b = x[:random.randint(max(1, len(x) - 4), len(x) - 1)]
  secret_key_b = x[:len(x) // 2]
  quo = binary_to_decimal(x) // binary_to_decimal(secret_key_b)
  rem = binary_to_decimal(x) % binary_to_decimal(secret_key_b)
  quo = decimal_to_binary(quo)
  rem = decimal_to_binary(rem)
  return quo, secret_key_a, secret_key_b, rem

if __name__ == '__main__':
  code = '00110110'
  print(encrypt(code))