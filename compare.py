import sys
import os
from tqdm import tqdm

def compare_text(f1, f2):
  with open(f1, 'r') as fp1:
    with open(f2, 'r') as fp2:
      for line1, line2 in tqdm(zip(fp1, fp2)):
        if line1 != line2:
          return False
  return True

if __name__ == '__main__':
  n = len(sys.argv)
  if n != 3:
    print('Usage: python3 decode.py [filename 1] [filename 2]')
    exit()

  filename1 = sys.argv[1]
  if not os.path.isfile(filename1):
    print('File not found: ' + filename1)
    exit()
  
  filename2 = sys.argv[2]
  if not os.path.isfile(filename2):
    print('File not found: ' + filename2)
    exit()
  
  print("*" * 40)
  print('Comparing files...')
  if compare_text(filename1, filename2):
    print('Verification successful!')
  else:
    print('Verification failed!')
  print("*" * 40)