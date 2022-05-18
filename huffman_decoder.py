from utility import Node, get_huffman_code
ind = 0


def deseralize(v):
  global ind
  if v[ind] == '|':
    ind += 1
    return None

  nw = Node(int(v[ind]))
  ind += 1
  nw.left = deseralize(v)
  nw.right = deseralize(v)
  return nw

def decode(code, root, mr):
  global ind
  if ind >= len(code):
    return chr(root.val)

  if not root.left and not root.right:
    return chr(root.val) + decode(code, mr, mr)
  
  if code[ind] == '0':
    ind += 1
    return decode(code, root.left, mr)
  else:
    ind += 1
    return decode(code, root.right, mr)

def main(code, lookup):
  global ind
  ind = 0
  root = deseralize(lookup.split(','))
  ind = 0
  d = decode(code, root, root)
  return d

if __name__ == '__main__':
  code = '111101001100'
  lookup = '394,297,100,|,|,197,98,|,|,99,|,|,97,|,|'
  print(main(code, lookup))


# 111101001100