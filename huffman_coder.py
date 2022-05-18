import heapq
from collections import Counter
from utility import Node


def get_freqency(s):
  freq = Counter(s)
  return freq

def get_huffman_tree(st):
  freq = get_freqency(st)
  heap = []
  for key in freq:
    nw = Node(ord(key))
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

def serialize(root):
  if root is None:
    return '|'
  return str(root.val) + ',' + serialize(root.left) + ',' + serialize(root.right)

def compress(st, mp):
  ret = ''
  for v in st:
    ret += mp[ord(v)]
  return ret

def dummy_tree():
  root = Node(0)
  root.left = Node(1)
  root.right = Node(2)
  root.left.left = Node(3)
  root.left.right = Node(4)
  root.right.left = Node(5)
  root.right.right = Node(6)
  return root

def huffman_encode(st):
  root = get_huffman_tree(st)
  mp = get_huffman_code(root)
  # root = dummy_tree()
  enc = compress(st, mp)
  loopup = serialize(root)
  return enc, loopup

if __name__ == '__main__':
  st = 'aaaabcd'
  print(huffman_encode(st))
