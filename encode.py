from encryption import encrypt
from huffman_coder import huffman_encode
from huffman_decoder import huffman_decode
import sys
import os


if __name__ == '__main__':
  # Check if the user has provided the correct number of arguments
  n = len(sys.argv)
  if n == 1:
    print('Usage: python3 encode.py [filename]')
    exit()

  # Get the filename from the command line
  filename = sys.argv[1]
  # Check if the file exists
  if not os.path.isfile(filename):
    print('File not found')
    exit()
  
  # Read the file
  with open(filename, 'r') as f:
    st = ''
    for line in f:
      st += line

    # print(st)
    # compress the file using huffman coding
    code, tree = huffman_encode(st)
    # encrypt the file using a key
    enc = encrypt(code)
    # print(enc)

    # Output logs
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

