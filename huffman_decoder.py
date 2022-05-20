from utility import Node
ind = 0
import sys
sys.setrecursionlimit(40000)

def deseralize(v):
  global ind
  if v[ind] == '|':
    ind += 1
    return None

  # 4.1.1 deseralize the tree from the string to tree
  nw = Node(int(v[ind]))
  ind += 1
  nw.left = deseralize(v)
  nw.right = deseralize(v)
  return nw

def decode_ite(code, root):
  st = [(code, root)]

  res = ''
  while len(st) > 0:
    code, nw = st.pop()
    if len(code) == 0:
      res += ''
      break
    
    curr = nw
    # 4.2.1 traverse the tree to find the leaf node
    for i, c in enumerate(code):
      if c == '0':
        curr = curr.left
      else:
        curr = curr.right
      # if found the leaf start from the root again
      if not curr.left and not curr.right:
        res += chr(curr.val)
        st.append((code[i+1:], root))
        break
  return res


def huffman_decode(code, lookup):
  global ind
  ind = 0
  # 4.1 deseralize the tree from the string to tree
  root = deseralize(lookup.split(','))
  ind = 0
  # 4.2 decode the code using the tree
  d = decode_ite(code, root)
  return d

if __name__ == '__main__':
  code = '111101001100'
  lookup = '394,297,100,|,|,197,98,|,|,99,|,|,97,|,|'
  print(huffman_decode(code, lookup))
