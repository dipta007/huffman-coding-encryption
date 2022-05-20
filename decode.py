from decryption import decrypt
from huffman_decoder import huffman_decode
from tqdm import tqdm
import sys
import os


if __name__ == '__main__':
  n = len(sys.argv)
  # Check if the user has provided the correct number of arguments
  if n == 1:
    print('Usage: python3 decode.py [filename]')
    exit()

  # Get the filename from the command line
  filename = sys.argv[1]
  # Check if the file exists
  if not os.path.isfile(filename):
    print('File not found')
    exit()
  
  # Read the file
  with open(filename, 'r') as f:
    rows = f.readlines()
    # Is that a valid file?
    if len(rows) != 5:
      print('Invalid file format')
      exit()
    
    # Strip new lines from all the lines
    rows = [row.strip() for row in rows]
    # Decrypt the file
    d = decrypt(rows[1], rows[2], rows[3], rows[4])
    # Decode the file
    txt = huffman_decode(d, rows[0])
    # txt = ''
    # print("*" * 40)
    # print("Decrypted text:")
    # print(txt)
    print("*" * 40)
    print('Your document is decrypted and uncompressed successfully!')
    dec_filename = 'decoded.txt'
    with open(dec_filename, 'w') as f:
      f.write(txt)
    print('Your decrypted file is:', dec_filename)
    print("*" * 40)
    print('To compare your file, run:')
    print('$ python3 compare.py filename1 filename2')
    print("*" * 40)
