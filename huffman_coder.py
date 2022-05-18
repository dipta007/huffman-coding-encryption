import heapq
from collections import Counter

class Node:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right
  
  def __lt__(self, other):
    return self.val <= other.val

def get_freqency(s):
  freq = Counter(s)
  return freq

def get_huffman_tree(st):
  freq = get_freqency(st)
  heap = []
  for key in freq:
    nw = Node(key)
    heapq.heappush(heap, (freq[key], nw))
  while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)

    nw = Node(left[1].val + right[1].val, left[1], right[1])
    heapq.heappush(heap, (left[0] + right[0], nw))
  return heapq.heappop(heap)[1]

def get_huffman_code(root, code=''):
  if root.left is None and root.right is None:
    return {root.val: code}
  d = {}
  if root.left:
    d.update(get_huffman_code(root.left, code + '0'))
  if root.right:
    d.update(get_huffman_code(root.right, code + '1'))
  return d

def get_lookup_table(mp):
  mx = max([len(v) for v in mp.values()])
  lens = ''
  tab = ''
  for k in mp.keys():
    lens += str(len(mp[k])) + '|'
    mp[k] = mp[k] + '0' * (mx - len(mp[k]))
    tab += str(ord(k)) + ':' + mp[k] + ':' + str(len(mp[k])) + '|'
  return tab

def compress(st, mp):
  ret = ''
  for v in st:
    ret += mp[v]
  return ret

def main(st):
  root = get_huffman_tree(st)
  mp = get_huffman_code(root)
  enc = compress(st, mp)
  loopup = get_lookup_table(mp)
  return enc, loopup

if __name__ == '__main__':
  st = 'Aaalgo'
  print(main(st))
