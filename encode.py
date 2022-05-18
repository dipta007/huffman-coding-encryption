from encryption import encrypt
from huffman_coder import huffman_encode
from huffman_decoder import huffman_decode
import sys
import os


if __name__ == '__main__':
  n = len(sys.argv)
  if n == 1:
    print('Usage: python3 encode.py [filename]')
    exit()

  filename = sys.argv[1]
  if not os.path.isfile(filename):
    print('File not found')
    exit()
  
  with open(filename, 'r') as f:
    st = ''
    for line in f:
      st += line

    # print(st)
    code, tree = huffman_encode(st)
    enc = encrypt(code)
    # print(enc)

    print("*" * 40)
    print('Your document is compressed & encrypted successfully!')
    enc_filename = 'encoded.txt'
    with open(enc_filename, 'w') as f:
      f.write(tree + '\n')
      f.write(enc[0] + '\n')
      f.write(enc[1] + '\n')
      f.write(enc[2] + '\n')
      f.write(enc[3] + '\n')
      
    print('Your compressed file is:', enc_filename)
    print("*" * 40)
    print('To decrypt your file, run:')
    print('$ python3 decode.py', enc_filename)
    print("*" * 40)

